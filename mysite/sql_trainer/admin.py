from django.contrib import admin

from .models import Book, Supply, Trip

admin.site.register(Book)
admin.site.register(Supply)
admin.site.register(Trip)