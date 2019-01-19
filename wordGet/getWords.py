import requests
import json
import random
import time
threshold = 0.5
random.seed(time.time())

def getWords(prefix):
    api = "https://api.datamuse.com/words?sp="+prefix+"*&md=fp"
    word = requests.get(api).json()
    bank = []
    for i in range(len(word)-1):
        if float(word[i]["tags"][len(word[i]["tags"])-1][2:])>threshold:
            if word[i]["word"].isalnum():
                if word[i]["word"] != prefix:
                    bank.append(word[i]["word"])
    word1 = bank[random.randint(0,len(bank))]
    word2 = bank[random.randint(0,len(bank))]
    return (word1, word2)
