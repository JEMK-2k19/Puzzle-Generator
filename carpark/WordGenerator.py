import csv, io
import requests
import random
import time
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
threshold = 1
random.seed(time.time())

class Puzzle:
    def __init__(self):
        self.word_generator = WordGenerator()
        self.answer = self.word_generator.get_answer()
        self.words = self.word_generator.words
        self.links = self.word_generator.links

    def check_answer(self, answer):
        if answer == self.answer:
            return True
        else:
            return False

class WordGenerator:
    def __init__(self):
        self.links = []
        while not self.links:
            self.words = []
            self.links = []
            self.prefix = self.get_random_prefix()
            self.wordlist = self.get_words(self.prefix)
            self.links = self.get_links(self.prefix, self.wordlist)

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
        if len(word) <= 10:
            return []
        return self.wordfilter(word, prefix)

    def get_links(self, prefix, bank):
        if len(bank) <= 2:
            return []
        link1 = self.find_link(bank)
        link2 = self.find_link(bank)
        if not link1 or not link2:
            return []
        newbank = [link1, link2]
        self.links = newbank
        return newbank

    def find_link(self, bank):
        newbank = []
        rand = random.randint(0, len(bank)-1)
        while len(newbank) == 0:
            api = "http://en.wikipedia.org/w/api.php?action=query&titles=" + bank[rand] + "&prop=pageimages&format=json&pithumbsize=1000"
            mono = requests.get(api).json()
            intm = mono["query"]["pages"][list(mono["query"]["pages"])[0]]
            if "thumbnail" in intm:
                newbank.append(intm["thumbnail"]["source"])
                self.words.append(bank[rand])
                bank.remove(bank[rand])
                return newbank[0]
            else:
                bank.remove(bank[rand])
                if len(bank) < 2:
                    return False
                rand = random.randint(0, len(bank) - 1)
        return newbank[0]

    def wordfilter(self, word, prefix):
        banks = set()
        words = []
        for i in self.rangelen(word):
            words.append(word[i]["word"])
        for i in self.rangelen(word):
            if float(word[i]["tags"][len(word[i]["tags"])-1][2:])>threshold:
                if word[i]["word"].isalpha():
                    if word[i]["word"] != prefix:
                        if word[i]["tags"][0]=='n':
                            if not("prop" in word[i]["tags"]):
                                if wnl.lemmatize(word[i]["word"]) in words:
                                    banks.add(wnl.lemmatize(word[i]["word"]))
                                else:
                                    banks.add(word[i]["word"])
        return list(banks)
        
    def rangelen(self, list):
        return range(len(list)-1)
    
    def get_answer(self):
        return self.prefix
