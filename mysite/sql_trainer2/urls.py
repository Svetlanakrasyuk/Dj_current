from django.urls import path

from .views import create_author

urlpatterns = [
    path('create/', create_author)
]