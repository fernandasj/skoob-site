# Generated by Django 2.1.1 on 2018-09-05 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=models.ImageField(default='imagens/none/no-img.jpg', upload_to='imagens/livros/', verbose_name='Imagem da capa'),
        ),
    ]
