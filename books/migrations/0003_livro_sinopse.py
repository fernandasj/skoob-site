# Generated by Django 2.1.1 on 2018-09-06 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180905_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='sinopse',
            field=models.TextField(default='Sem Sinopse', max_length=700, verbose_name='Sinopse'),
        ),
    ]