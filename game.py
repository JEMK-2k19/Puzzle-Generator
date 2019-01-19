import os

class Game:
    """A sample Employee class"""

    def __init__(self, player1):
        self.player1 = player1
        self.player2 = none
        self.p1Score = 0
        self.p2Score = 0
        self.gameId = os.random()
        isFull = false

    def setPlayer2(self, player2):
        self.player2 = player2

    def setFull(self):
        self.isFull = true

    def addP1Score(self, amount):
    	p1Score = p1Score + amount

    def addP2Score(self, amount):
    	p2Score = p2Score + amount

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.player1, self.player2, self.p1Score, self.p2Score, self.gameId, self.isFull)