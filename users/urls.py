from django.urls import path, include
from .views import registerUser, UserEdit

app_name = 'users'
urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', registerUser, name='registerUser'),
    path('<int:pk>/edit/', UserEdit, name='editUser'),
]
