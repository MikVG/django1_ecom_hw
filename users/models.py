from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=50, unique=True, verbose_name='почта', help_text='введите почту')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', help_text='прикрепите аватар',
                               blank=True, null=True)
    phone = models.CharField(max_length=35, verbose_name='телефон',help_text='введите номер телефона',
                             blank=True, null=True)
    country = models.CharField(max_length=25, verbose_name='страна',help_text='укажите страну',
                               blank=True, null=True)
    token = models.CharField(max_length=50, verbose_name='токен',
                             blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
