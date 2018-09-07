from .models import Livro
from django.shortcuts import render
import operator
from django.db.models import Q


def Search(request):
    try:
        query = request.POST['search']
        result1 = 'Sua busca:';
        result2 = ', retornou os seguintes resultados.';
        livros = Livro.objects.filter(titulo__contains=query)
        return render(request, 'results.html', {'livros':livros, 'query':query, 'result1':result1, 'result2':result2})
    except KeyError:
        return render(request, 'home.html')
