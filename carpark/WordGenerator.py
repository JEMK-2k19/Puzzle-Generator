import csv, io
import random

def read_csv(fname):
    new = []
    with open(fname, encoding = 'utf-8') as f:
        for row in csv.reader(f):
            new.append(row)
    return new

def get_wordlist():
    data = read_csv("ELP Data.csv")
    data[0][0] = data[0][0][1:]
    data = list(map(lambda x: x[0], data))
    return data

def get_random_prefix():
    wordlist = get_wordlist()
    random_index = random.randint(0, len(wordlist))
    prefix = wordlist[random_index][:3]
    return prefix

for i in range(10):
    print(get_random_prefix())