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
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='books')

    def __str__(self):
        return self.title


class City(models.Model):
    name_city = models.CharField(max_length=30)
    days_delivery = models.IntegerField()

    def __str__(self):
        return self.name_city


class Client(models.Model):
    name_client = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name_client


class Buy(models.Model):
    buy_description = models.CharField(max_length=100, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)


class BuyBook(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Step(models.Model):
    name_step = models.CharField(max_length=30)

    def __str__(self):
        return self.name_step


class BuyStep(models.Model):
    buy = models.ForeignKey(Buy, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    date_step_beg = models.DateField(blank=True, null=True)
    date_step_end = models.DateField(blank=True, null=True)
