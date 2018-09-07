from django.urls import path

from .views import book_info, reading_books, read_books, readed_books, myBooks

app_name = 'books'

urlpatterns = [
	path('book_info/<int:pk>', book_info, name='book_info'),
    path('ler/', read_books, name='read_books'),
    path('lendo/', reading_books, name='reading_books'),
    path('lido/', readed_books, name='readed_books'),
    path('myBooks/', myBooks, name='myBooks')
]
