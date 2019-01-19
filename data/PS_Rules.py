import random

#lexicon_jap = dict(map(lambda x: x[0:2], lexicon))
#lexicon_chi = dict(map(lambda x: (x[0],) + (x[2],), lexicon))

##words = nltk.corpus.brown.tagged_words(tagset = "universal")
##text = input()
##text = nltk.word_tokenize(text)
##words = nltk.pos_tag(text)
##lexicon = {}
##for word in words:
##    if word[1] not in lexicon:
##        lexicon[word[1]] = []
##    if word[0] not in lexicon[word[1]]:
##        lexicon[word[1]].append(word[0])
nouns = [("boy", "男の子","男孩"), ("girl","女の子","女孩"), ("cat","猫","猫"), ("banana","バナナ","香蕉"),("dog", "犬","狗")]
verbs = [("saw","見た","看见了"), ("ate","食べた","吃了")]
verbs_i = [("slept","寝た","睡觉了")]
verbs_cop = [("is","です","是")]
det = [("the","","那个"), ("a","","一个")]
adj = [("small","小さい","小"),("big","大きい","大")]
prep = [("on","の上","上的"), ("in","の中","里的")]
adv = [("slowly",), ("happily",)]
case = [("nom","は",""),("acc","を",""),("dat","",""),("gen","の","")]
comp = [("that","","的")]

lexicon = nouns + verbs + det + adj + case + prep + verbs_cop + verbs_i + adv + [("","","")]

class XP:
    def __init__(self, X, head):
        self.first = None
        self.second = None
        self.head = head
        self.dic = {"S": [[lambda: DP("nom")], [lambda: VP(random.randrange(3))]],
         "VP": [[lambda: self.lex("Vc"), lambda: self.lex("Vi"), lambda: self.lex("V")], [lambda: self.lex("Adj"), lambda: "", lambda: DP("acc")],
                [lambda: VP(random.randrange(3)), lambda: VP(random.randrange(3), False)], [lambda: self.lex("Adv")],[lambda: PP("VP")]],
         "DP": [[lambda: self.lex("D")], [lambda: NP()]],
         "NP": [[lambda: self.lex("N")], [lambda: ""], [lambda: NP(), lambda: NP(False)], [lambda: self.lex("Adj")], [lambda: PP("NP"),]],
         "PP": [[lambda: self.lex("P")], [lambda: DP("dat")]], #dat only for VP adjunct
         "CP": [[lambda: self.lex("C")], [lambda: S()]]
        }
        self.gen(X)
        self.nouns = nouns

    def gen(self, X):
        functions = self.dic[X]
        terminal = bool(random.randrange(3))
        if terminal or len(functions) == 2:
            if isinstance(self, VP):
                self.vp_gen()
            elif isinstance(self, PP):
                self.pp_gen()
            else:
                self.first = random.choice(functions[0])()
                self.second = random.choice(functions[1])()
        else:
            if self.head:
                self.first = random.choice(functions[2])()
                self.second = random.choice(functions[4])()
            else:
                self.first = random.choice(functions[3])()
                self.second = functions[2][1]()

    def japanese(self):
        left = [type(DP(None)), type(VP(0)), type(PP("NP"))]
        right = [type(S()), type(NP())]
        if type(self) in left or (type(self) == type(NP()) and self.head):
            self.first, self.second = self.second, self.first
        if isinstance(self.first, DP):
            self.first = self.first.japanese() + lexicon_jap[self.first.case]
        elif isinstance(self.first, PP):
            self.first = self.first.japanese() + self.first.adjunct_type
        elif type(self.first) == str:
            self.first = lexicon_jap[self.first]
        else:
            self.first = self.first.japanese()
        if isinstance(self.second, DP):
            self.second = self.second.japanese() + lexicon_jap[self.second.case]
        elif isinstance(self.second, PP):
            self.second = self.second.japanese() + self.second.adjunct_type
        elif type(self.second) == str:
            self.second = lexicon_jap[self.second]
        else:
            self.second = self.second.japanese()
        return self.print()

    def chinese(self):
        left = [type(PP("NP"))]
        if type(self) in left or (type(self) == type(NP()) and self.head):
            self.first, self.second = self.second, self.first
        if type(self.first) == str:
            self.first = lexicon_chi[self.first]
        else:
            self.first = self.first.chinese()
        if type(self.second) == str:
            self.second = lexicon_chi[self.second]
        else:
            self.second = self.second.chinese()
        return self.print()

    def lex(self, X):
        dic = {"N": nouns, "V": verbs, "D": det, "Adj": adj, "P": prep, "Adv" : adv, "C": comp, "Vi": verbs_i, "Vc": verbs_cop}
        #tags = {"N": "NN", "V": "VBD", "D": "DT", "Adj": "JJ", "P": "IN", "Adv" : adv, "C": comp, "Vi": verbs_i, "Vc": verbs_cop}
        #return random.choice(dic[tags[X]])[0]
        return random.choice(dic[X])[0]

    def print(self):
        result = ""
        if type(self.first) == str:
            result += self.first + " "
        else:
            result += self.first.print() + " "
        if type(self.second) == str:
            result += self.second + " "
        else:
            result += self.second.print() + " "
        result = result.split()
        string = ""
        for i in result:
            string += i + " "
        return string[:-1]

class NP(XP):
    def __init__(self, *head):
        head = head[0] if head != () else bool(random.randrange(2))
        super().__init__("NP", head)
        #head is true if left "headed"

class VP(XP):
    def __init__(self, valence, *head):
        self.valence = valence #0 if copula verb
        head = head[0] if head != () else bool(random.randrange(2))
        super().__init__("VP", head)

    def vp_gen(self):
        self.first = self.dic["VP"][0][self.valence]()
        self.second = self.dic["VP"][1][self.valence]()

class S(XP):
    def __init__(self):
        super().__init__("S", False)

class DP(XP):
    def __init__(self, case):
        self.case = case
        super().__init__("DP", True)

class PP(XP):
    def __init__(self,adjunct_type):
        self.adjunct_type = "で" if adjunct_type == "VP" else "の"
        super().__init__("PP", True)

    def pp_gen(self):
        self.first = random.choice(self.dic["PP"][0])()
        self.second = self.dic["PP"][1][0]()

class CP(XP):
    def __init__(self):
        super().__init__("CP", True)

def run():
    result = []
    for i in range(10):
        new = XP("S", False)
        result.append(new.print())
        #print(new.japanese())
        #print(new.chinese())
    return result
