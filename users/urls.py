from django.urls import path, include
from .views import registerUser

app_name = 'users'
urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', registerUser, name='registerUser'),
]
