from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import UserBook, Livro


def home(request):
    books = Livro.objects.all()
    return render(request, 'home.html', {'books': books})

def book_info(request, pk):
    books = Livro.objects.get(pk=pk)
    print(books)
    return render(request, 'books/book.html', {'books': books})

@login_required(login_url='/accounts/login/')
def myBooks(request):
    books = UserBook.objects.filter(user=request.user)
    return render(request, 'books/myBooks.html', {'books': books})


@login_required(login_url='/accounts/login/')
def reading_books(request):
    books = UserBook.objects.filter(user=request.user, status=UserBook.LENDO)
    return render(request, 'books/books-lendo.html', {'books': books})


@login_required(login_url='/accounts/login/')
def readed_books(request):
    books = UserBook.objects.filter(user=request.user, status=UserBook.LIDO)
    return render(request, 'books/books-lidos.html', {'books': books})


@login_required(login_url='/accounts/login/')
def read_books(request):
    books = UserBook.objects.filter(user=request.user, status=UserBook.LER)
    return render(request, 'books/books-ler.html', {'books': books})
