from django.db import models

class Carpark(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

class Route(models.Model):
    start = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)

class Question(models.Model):
    answer = models.CharField(max_length=100)

class joinGameForm(models.Model):
    name = models.CharField(max_length=100)
    access_code = models.CharField(max_length=8)

class Player(models.Model):
    name = models.CharField(max_length=100)

class Game(models.Model):
    game_id = models.CharField(max_length=8)

    @classmethod
    def create(cls, game_id):
        book = cls(game_id=game_id)
        # do something with the book
        return book

class CurrentRound(models.Model):
    word1 = models.CharField(max_length=100)
    word2 = models.CharField(max_length=100)
    link1 = models.CharField(max_length=1000)
    link2 = models.CharField(max_length=1000)
    points = models.IntegerField()
    answer = models.CharField(max_length=100)
    question_no = models.IntegerField()
    id = models.IntegerField(primary_key=True)

    #@classmethod
    #def create(cls, word1, word2):
    #    round = cls(prev_word1 = word1, prev_word2 = word2, points=0)
    #    # do something with the book
    #   return round

    def change_words(self, word1, word2):
        self.prev_word1 = word1
        self.prev_word2 = word2
        # do something with the book
        return self

    def add_points(self, points):
        self.points = self.points + points
        # do something with the book
        return self

