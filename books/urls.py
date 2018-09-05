from django.urls import path

from .views import my_books


app_name = 'books'

urlpatterns = [
    path('ler/', my_books, name='my_books'),
]
