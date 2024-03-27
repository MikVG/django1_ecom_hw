from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True, verbose_name='почта', help_text='введите почту')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', help_text='прикрепите аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон',help_text='введите номер телефона', **NULLABLE)
    country = models.CharField(max_length=25, verbose_name='страна',help_text='укажите страну', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
