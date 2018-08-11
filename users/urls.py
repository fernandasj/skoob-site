from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import registerUser


app_name = 'users'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', registerUser, name='registerUser'),
]
