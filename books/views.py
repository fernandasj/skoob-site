
from django.shortcuts import redirect, render
import operator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Livro, UserBook


def Search(request):
    try:
        query = request.POST['search']
        result1 = 'Sua busca:';
        result2 = ', retornou os seguintes resultados.';
        result3 = 'Esse livro não está cadastrado.';

        livros = Livro.objects.filter(titulo__contains=query)
        if livros.exists():
            return render(request, 'results.html', {'livros':livros, 'query':query, 'result1':result1, 'result2':result2})
        else:
            return render(request, 'results.html', {'query':query, 'result1':result1, 'result2':result2, 'result3':result3})
    except KeyError:
        return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def statusBook(request, pk, status):
    try:
        book = UserBook.objects.get(user=request.user, livro=pk)
        book.status = status
        book.save()
    except UserBook.DoesNotExist:
        li = Livro.objects.get(pk=pk)
        book = UserBook(user=request.user, livro=li, status=status)
        book.save()
    userbook = UserBook.objects.get(user=request.user, livro=pk)
    books = Livro.objects.get(pk=pk)
    return render(request, 'books/book.html', {'books': books, 'userbook':userbook})

def home(request):
    books = Livro.objects.all()
    return render(request, 'home.html', {'books': books})

def book_info(request, pk):
    books = Livro.objects.get(pk=pk)
    ###Removi user=request.user do filtro
    userbook = UserBook.objects.filter(livro=pk)
    return render(request, 'books/book.html', {'books': books, 'userbook':userbook})

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
