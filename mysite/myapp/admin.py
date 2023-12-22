from django.contrib import admin

from .models import Author, Genre, Producer, Book, MyModelA


class MyModelAAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug_a": ["char_a"]}


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Producer)
admin.site.register(Book)
admin.site.register(MyModelA, MyModelAAdmin)
