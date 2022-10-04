from django.db import models


class Author(models.Model):
    nameAuthor = models.CharField(max_length=20)


class Genre(models.Model):
    genreName = models.CharField(max_length=15)


class Book(models.Model):
    BookName = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Reader(models.Model):
    book = models.ManyToManyField(Book)
