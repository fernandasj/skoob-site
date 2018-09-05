from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Livro, UserBook


@login_required(login_url='/accounts/login/')
def home(request):
    photos = Livro.objects.all()
    return render(request, 'home.html', {'photos': photos})


def my_books(request):
    books = UserBook.objects.filter(user=request.user, status=UserBook.LER)
    return render(request, 'books-ler.html', {'books': books})
