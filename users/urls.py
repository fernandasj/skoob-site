from django.urls import path, include
from .views import registerUser, profile

app_name = 'users'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', registerUser, name='registerUser'),
    path('profile/', profile, name='profile'),
]
