from .models import Livro
from django.shortcuts import render
import operator
from django.db.models import Q


def Search(request):
    try:
        q = request.GET['search']
        livros = Livro.objects.filter(titulo__search=q)
        return render_to_response('results.html', {'livros':livros, 'q':q})
    except KeyError:
        return render_to_response('results.html')
