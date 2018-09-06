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

def reading_books(request):
    books = UserBook.objects.filter(user=request.user, status=UserBook.LENDO)
    return render(request, 'books-lendo.html', {'books': books})

def read_books(request):
    books = UserBook.objects.filter(user=request.user, status=UserBook.LIDO)
    return render(request, 'books-lidos.html', {'books': books})

