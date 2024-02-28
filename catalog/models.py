from datetime import datetime

from django.db import models
from django.utils import connection

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    """
    класс для описания модели Category
    """
    name = models.CharField(max_length=100, verbose_name='категория')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """
    класс для описания модели Product
    """
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена за единицу')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    #manufactured_at = models.DateTimeField(default=datetime.now, verbose_name='дата производства')

    def __str__(self):
        return f'{self.name} {self.description} {self.category} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Blog(models.Model):
    """
    класс для описания блога
    """
    title = models.CharField(max_length=250, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='preview/', verbose_name='превью', **NULLABLE)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title} {self.is_published} {self.create_date}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
