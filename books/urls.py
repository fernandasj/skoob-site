from django.urls import path, include
from .views import Search

app_name = 'books'
urlpatterns = [
    path('search/', Search, name='search'),
]
