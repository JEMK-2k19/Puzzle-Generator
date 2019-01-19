class Player:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Player('{}'".format(self.name)