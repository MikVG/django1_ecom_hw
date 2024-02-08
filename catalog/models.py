from django.db import models


class Product(models.Model):
    """
    класс для описания модели Product
    """
    pass

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    """
    класс для описания модели Category
    """
    pass

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
