from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class Dictionary(models.Model):
    name = models.CharField(max_length=100)
    pages = models.IntegerField()
    author = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.IntegerField()
    rating = models.FloatField()

