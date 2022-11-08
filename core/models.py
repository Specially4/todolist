from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_of_birth = models.DateTimeField()
    age = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
