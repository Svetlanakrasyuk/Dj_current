from django.urls import path

from . import views
from .views import IndexView

urlpatterns = [
    path("", views.index, name="index"),
    path('view/', IndexView.as_view())
]