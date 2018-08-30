from django.contrib import admin
from .models import Livro, UserBook

class BookAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'autor', 'editora')

admin.site.register(Livro, BookAdmin)


class UserBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'livro', 'status')

admin.site.register(UserBook, UserBookAdmin)


