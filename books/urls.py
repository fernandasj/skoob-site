from django.urls import path, include
from .views import Search
# from .views import registerBook


app_name = 'books'
urlpatterns = [
    path('search/', Search, name='search'),
    # path('register/', registerUser, name='registerBook'),
]
