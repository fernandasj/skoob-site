from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Livro


@login_required(login_url='/accounts/login/')
def home(request):
    photos = Livro.objects.all()
    return render(request, '../templates/home.html', {'photos': photos})


