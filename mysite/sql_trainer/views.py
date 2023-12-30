import datetime

from django.db.models import F, FloatField, Case, When, Q, Count, Sum, Min, Max, Avg, Subquery, Value, DecimalField, \
    DateField, IntegerField
from django.db.models.functions import Cast, ExtractDay
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Book, Supply, Trip


class BookView(generic.ListView):
    template_name = 'sql_trainer/index.html'
    context_object_name = 'books'

    def get_queryset(self):
        qs = (Trip.objects.annotate(Длительность=F('date_last') - F('date_first') + datetime.timedelta(days=1))
              .values()
              .annotate(длительность_в_сутках=Cast('Длительность', output_field=IntegerField())/60/60/24/1000000)
              .values()
              .annotate(cost=F('длительность_в_сутках') * F('per_diem'))
              .filter(date_first__month__in=[2,3])
              .order_by('name', '-cost'))
        return qs


def create_trips(request):
    Trip.objects.all().delete()
    data = [(1, 'Баранов П.Е.','Москва',700 , '2020-01-12', '2020-01-17'),
    (2, 'Абрамова К.А.','Владивосток',450 , '2020-01-14', '2020-01-27'),
    (3, 'Семенов И.В.','Москва',700 , '2020-01-23', '2020-01-31'),
    (4, 'Ильиных Г.Р.','Владивосток', 450, '2020-01-12', '2020-02-02'),
    (5, 'Колесов С.П.','Москва',700 , '2020-02-01', '2020-02-06'),
    (6, 'Баранов П.Е.','Москва', 700, '2020-02-14', '2020-02-22'),
    (7, 'Абрамова К.А.','Москва', 700, '2020-02-23', '2020-03-01'),
    (8, 'Лебедев Т.К.','Москва', 700, '2020-03-03', '2020-03-06'),
    (9, 'Колесов С.П.','Новосибирск',450 , '2020-02-27', '2020-03-12'),
    (10, 'Семенов И.В.','Санкт-Петербург',700 , '2020-03-29', '2020-04-05'),
    (11, 'Абрамова К.А.','Москва',700 , '2020-04-06', '2020-04-14'),
    (12, 'Баранов П.Е.','Новосибирск',450 , '2020-04-18', '2020-05-04'),
    (13, 'Лебедев Т.К.','Томск',450 , '2020-05-20', '2020-05-31'),
    (14, 'Семенов И.В.','Санкт-Петербург',700 , '2020-06-01', '2020-06-03'),
    (15, 'Абрамова К.А.','Санкт-Петербург', 700, '2020-05-28', '2020-06-04'),
    (16, 'Федорова А.Ю.','Новосибирск',450 , '2020-05-25', '2020-06-04'),
    (17, 'Колесов С.П.','Новосибирск', 450, '2020-06-03', '2020-06-12'),
    (18, 'Федорова А.Ю.','Томск', 450, '2020-06-20', '2020-06-26'),
    (19, 'Абрамова К.А.','Владивосток', 450, '2020-07-02', '2020-07-13'),
    (20, 'Баранов П.Е.','Воронеж', 450, '2020-07-19', '2020-07-25')]
    # data = [{'title': 'Мастер и Маргарита', 'author': 'Булгаков М.А.',
    #          'price': '670.99', 'amount': 3},
    #         {'title': 'Белая гвардия', 'author': 'Булгаков М.А.',
    #          'price': '540.50', 'amount': 5},
    #         {'title': 'Идиот', 'author': 'Достоевский Ф.М.',
    #          'price': '460.00', 'amount': 10},
    #         {'title': 'Братья Карамазовы', 'author': 'Достоевский Ф.М.',
    #          'price': '799.01','amount': 3},
    #         {'title': 'Стихотворения и поэмы', 'author': 'Есенин С.А.',
    #          'price': '650.00', 'amount': 15}]
    Trip.objects.bulk_create([Trip(*q) for q in data])
    return HttpResponse(status=201)


