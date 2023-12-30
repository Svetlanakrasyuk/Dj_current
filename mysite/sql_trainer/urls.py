from django.urls import path

from .views import BookView, create_trips

urlpatterns=[
    path('', BookView.as_view()),
    path('create/', create_trips)
]
