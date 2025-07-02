from django.urls import path

from .views import create_author, MyView

urlpatterns = [
    path('create/', create_author),
    path('', MyView.as_view())
]