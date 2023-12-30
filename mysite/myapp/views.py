from django.db.models import Count, F
from django.shortcuts import render

from django.http import HttpResponse
from django.views import generic

from .models import Author, Genre, Producer, Book


def index(request):
    aut = Author.objects.get(id=1)
    # gen = Genre.objects.get(id=1)
    # prod = Producer.objects.get(id=5)
    # book = Book.objects.get(name='book from view')
    # book4= Book.objects.create(name='book from view', book_author=aut, book_producer=prod)
    # output =book4.book_genre.set([gen])
    # output = aut.book_set.create(name='book from view', book_author=aut, book_producer=prod)
    return HttpResponse(aut)


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'my_context'

    def get_queryset(self):
        # output = Author.objects.annotate(number_books=Count('book')).values('book__name', 'number_books').filter(id=1)
        # output = Author.objects.values('name', 'book__name', number_books=Count('book'))
        # output_2 = Author.objects.values('name', 'book__name').annotate(number_books=Count('book'))
        output = Book.objects.filter(name__exact='book1')
        # print(output_2)
        return output
