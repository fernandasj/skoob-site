from django.urls import path

from .views import reading_books, read_books, readed_books

app_name = 'books'

urlpatterns = [
    path('ler/', read_books, name='read_books'),
    path('lendo/', reading_books, name='reading_books'),
    path('lido/', readed_books, name='readed_books'),
]
