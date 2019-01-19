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

