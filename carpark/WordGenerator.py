import csv, io
import random
import requests
import random
import time
threshold = 0.5
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
        api = "https://api.datamuse.com/words?sp=" + prefix + "*&md=fp"
        word = requests.get(api).json()
        bank = []
        for i in range(len(word) - 1):
            if float(word[i]["tags"][len(word[i]["tags"]) - 1][2:]) > threshold:
                if word[i]["word"].isalnum():
                    if word[i]["word"] != prefix:
                        bank.append(word[i]["word"])
        if bank == [] or len(bank) < 2:
            return []
        self.word1 = bank[random.randint(0, len(bank))]
        self.word2 = bank[random.randint(0, len(bank))]
        return [self.word1, self.word2]

    def get_answer(self):
        return self.prefix
