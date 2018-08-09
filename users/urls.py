from django.urls import path, include
from django.views.generic.base import TemplateView

# from .views import index


urlpatterns = [
    # path('', index, name='index'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
]
