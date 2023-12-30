from django.db import models


class Author(models.Model):
    name_author= models.CharField(max_length=50)

    def __str__(self):
        return self.name_author


class Genre(models.Model):
    name_genre = models.CharField(max_length=30)

    def __str__(self):
        return self.name_genre


class Book(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='genre')

    def __str__(self):
        return self.title
