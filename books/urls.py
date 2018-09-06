from django.urls import path

from .views import my_books
from .views import reading_books
from .views import read_books

app_name = 'books'

urlpatterns = [
    path('ler/', my_books, name='my_books'),
    path('lendo/', reading_books, name='reading_books'),
    path('lido/', read_books, name='read_books'),
]
