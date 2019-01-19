import csv, io
import random
import requests
import random
import time
from nltk.stem import SnowballStemmer
stemmer = SnowballStemmer("english")
threshold = 1
random.seed(time.time())

class Puzzle:
    def __init__(self):
        self.word_generator = WordGenerator()
        self.answer = self.word_generator.get_answer()
        self.words = self.word_generator.words

    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False

class WordGenerator:
    def __init__(self):
        self.words = []
        while not self.words:
            self.prefix = self.get_random_prefix()
            self.words = self.get_words(self.prefix)

    def read_csv(self, fname):
        new = []
        with open(fname, encoding = 'utf-8') as f:
            for row in csv.reader(f):
                new.append(row)
        return new

    def get_wordlist(self):
        data = self.read_csv("carpark/ELP Data.csv")
        data[0][0] = data[0][0][1:]
        data = list(map(lambda x: x[0], data))
        return data

    def get_random_prefix(self):
        wordlist = self.get_wordlist()
        random_index = random.randint(0, len(wordlist))
        prefix = wordlist[random_index][:3]
        return prefix

    def get_words(self, prefix):
        api = "https://api.datamuse.com/words?sp=" + prefix + "*&md=fpd"
        word = requests.get(api).json()
        banks = set()
        words = []
        if len(word) <= 20:
            return []
        for i in range(len(word)-1):
            words.append(word[i]["word"])
        for i in range(len(word)-1):
            if float(word[i]["tags"][len(word[i]["tags"])-1][2:])>threshold:
                if word[i]["word"].isalpha():
                    if word[i]["word"]!=prefix:
                        if word[i]["tags"][0]=='n':
                            if stemmer.stem(word[i]["word"]) in words:
                                banks.add(stemmer.stem(word[i]["word"]))
                            else:
                                banks.add(word[i]["word"])
        bank = list(banks)
        if bank == [] or len(bank) < 2:
            return []
        rand1 = random.randint(0,len(bank)-1)
        rand2 = random.randint(0,len(bank)-1)
        while rand2 == rand1:
            rand2 = random.randint(0,len(bank)-1)
        self.word1 = bank[rand1]
        self.word2 = bank[rand2]
        return [self.word1, self.word2]

    def get_answer(self):
        return self.prefix
