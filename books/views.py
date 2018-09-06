from django.shortcuts import render
import operator
from django.db.models import Q

from django.contrib.auth.models import Books

class BooksSearchListView(BooksListView):

    paginate_by = 10

    def get_queryset(self):
        result = super(BooksSearchListView, self).get_queryset()

        query = self.request.GET.get('search')
        if query:
            query_list = query.split()
            result = result.filter(
                books__titulo__exact = query
            )

        return result
