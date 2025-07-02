from django.db.models import Prefetch, F, Sum, Q, Max, Subquery, OuterRef, Count, DecimalField, IntegerField, Case, When
from django.db.models.functions import Cast
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Author, Book, Genre, City, Client, Buy, BuyBook, Step, BuyStep

a = 'Не удалять'
# внес необходимые изменения
class MyView(generic.ListView):
    context_object_name = 'my_context'
    template_name = 'sql_trainer2/index.html'

    def get_queryset(self):
        sum_count = Genre.objects.annotate(Количество=Sum(F('books__buybook__amount')))
        max_count = sum_count.aggregate(Max(F('Количество')))
        qs = sum_count.filter(Количество=max_count['Количество__max']).values()
        return qs


def create_author(request):
    Author.objects.all().delete()
    Book.objects.all().delete()
    data = [(1, 'Булгаков М.А.'), (2, 'Достоевский Ф.М.',), (3, 'Есенин С.А.',), (4, 'Пастернак Б.Л.',)]
    Author.objects.bulk_create([Author(*q) for q in data])
    data_book = [(1, 'Мастер и Маргарита', 670.99, 3,	1, 1),
     (2, 'Белая гвардия', 540.50, 5, 1, 1),
     (3, 'Идиот', 460.00, 10, 2, 1),
     (4, 'Братья Карамазовы', 799.01, 3, 2, 1),
     (5, 'Игрок', 480.50, 10, 2, 1),
     (6, 'Стихотворения и поэмы', 650.00 ,15, 3, 2),
     (7, 'Черный человек', 570.20, 6, 3, 2),
     (8, 'Лирика', 518.99, 2, 4, 2)]
    Book.objects.bulk_create([Book(*q) for q in data_book])
    City.objects.all().delete()
    data_city = [
        (1, 'Москва', 5),
        (2, 'Санкт - Петербург', 3),
        (3, 'Владивосток', 12)
    ]
    City.objects.bulk_create([City(*q) for q in data_city])
    Client.objects.all().delete()
    data_client = [
        (1,    'Баранов Павел',    3,    'baranov@test'),
        (2,    'Абрамова Катя',    1,    'abramova@test'),
        (3,    'Семенонов Иван',    2,    'semenov@test'),
        (4,    'Яковлева Галина',    1,    'yakovleva@test'),
    ]
    Client.objects.bulk_create([Client(*q) for q in data_client])
    Buy.objects.all().delete()
    data_buy = [
        (1,    'Доставка только вечером',    1),
        (2,    '',    3),
        (3,    'Упаковать каждую книгу по отдельности',    2),
        (4,    '',    1),
    ]
    Buy.objects.bulk_create([Buy(*q) for q in data_buy])
    BuyBook.objects.all().delete()
    data_buy_book = [
        (1,    1,    1,    1),
        (2,    1,    7,    2),
        (3,    1,    3,    1),
        (4,    2,    8,    2),
        (5,    3,    3,    2),
        (6,    3,    2,    1),
        (7,    3,    1,    1),
        (8,    4,    5,    1),
    ]
    BuyBook.objects.bulk_create([BuyBook(*q) for q in data_buy_book])
    Step.objects.all().delete()
    data_step = [
        (1,    'Оплата'),
        (2,    'Упаковка'),
        (3,    'Транспортировка'),
        (4,    'Доставка'),
    ]
    Step.objects.bulk_create([Step(*q) for q in data_step])
    BuyStep.objects.all().delete()
    data_buy_step = [
        (1,     1,    1,    '2020-02-20',    '2020-02-20'),
        (2,    1,    2,    '2020-02-20',    '2020-02-21'),
        (3,    1,    3,    '2020-02-22',    '2020-03-07'),
        (4,    1,    4,    '2020-03-08',    '2020-03-08'),
        (5,    2,    1,    '2020-02-28',    '2020-02-28'),
        (6,    2,    2,    '2020-02-29',    '2020-03-01'),
        (7,    2,    3,    '2020-03-02', None),
        (8,    2,    4, None, None),
        (9,    3,    1,    '2020-03-05',    '2020-03-05'),
        (10,    3,    2,    '2020-03-05',    '2020-03-06'),
        (11,    3,    3,    '2020-03-06',    '2020-03-10'),
        (12,    3,    4,    '2020-03-11', None),
        (13,    4,    1,    '2020-03-20', None),
        (14,    4,    2, None, None),
        (15,    4,    3, None, None),
        (16,    4,    4, None, None),
    ]
    BuyStep.objects.bulk_create([BuyStep(*q) for q in data_buy_step])
    return HttpResponse(status=201)
