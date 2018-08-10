from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profiles'
    )

    name = models.CharField(
        max_length=254
    )

    gender = models.CharField(
        max_length=10
    )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
