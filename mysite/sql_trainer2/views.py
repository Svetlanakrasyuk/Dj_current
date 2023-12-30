from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Author


class CreateAuthorView(generic.ListView):
    pass

def create_author(request):
    Author.objects.all().delete()
    data = [(1, 'Булгаков М.А.'), (2, 'Достоевский Ф.М.',), (3, 'Есенин С.А.',), (4, 'Пастернак Б.Л.',)]
    Author.objects.bulk_create([Author(*q) for q in data])
    return HttpResponse(status=201)
