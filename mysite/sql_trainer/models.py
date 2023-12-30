from django.db import models


# class Author(models.Model):
#     name_author = models.CharField(max_length=255)
#
#
# class Genre(models.Model):
#     name_genre = models.CharField(max_length=255)
#

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    author = models.CharField(max_length=255, verbose_name='Author')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')
    amount = models.IntegerField(verbose_name='Amount')

    def __str__(self):
        return self.title


class Supply(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    author = models.CharField(max_length=255, verbose_name='Author')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')
    amount = models.IntegerField(verbose_name='Amount')

    def __str__(self):
        return self.title


class Trip(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=25)
    per_diem = models.DecimalField(max_digits=8, decimal_places=2)
    date_first = models.DateField()
    date_last = models.DateField()

    def __str__(self):
        return str(self.name) + ' ' + str(self.city)
