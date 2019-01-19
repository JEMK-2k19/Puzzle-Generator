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