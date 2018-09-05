from django.contrib.auth.models import User
from django.db import models

class Livro(models.Model):

    capa = models.ImageField(
        'Imagem da capa',
        upload_to='imagens/livros/',
        default='imagens/none/no-img.jpg'
    )

    titulo = models.CharField(
        'Nome',
        max_length=40
    )

    genero = models.CharField(
        'Genero',
        max_length=100
    )

    autor = models.CharField(
        'Autor',
        max_length=50
    )

    editora = models.CharField(
        'Editora',
        max_length=50
    )

    paginas = models.IntegerField(
        'Número de páginas'
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'livro'
        verbose_name_plural = 'livros'


class UserBook(models.Model):
    LER = 'LER'
    LENDO = 'LENDO'
    LIDO = 'LIDO'
    STATUS_BOOK = (
        (LER, 'Ler'),
        (LENDO, 'Lendo'),
        (LIDO, 'Lido'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='usersbooks'
    )

    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='livros'
    )

    status = models.CharField(
        max_length=15,
        choices=STATUS_BOOK,
        default=LER
    )

    def __str__(self):
        return self.livro.titulo

    class Meta:
        verbose_name = 'userbook'
        verbose_name_plural = 'usersbooks'
