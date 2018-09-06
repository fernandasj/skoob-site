from django.urls import path, include
from .views import BooksSearchListView, home

app_name = 'books'
urlpatterns = [
    path('books_search_list_view', BooksSearchListView, name='BooksSearchListView'),
]
