from django.contrib import admin

from .models import Author, Genre, Book, City, Client, Buy, BuyBook, Step, BuyStep

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(City)
admin.site.register(Client)
admin.site.register(Buy)
admin.site.register(BuyBook)
admin.site.register(Step)
admin.site.register(BuyStep)
