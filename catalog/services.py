from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Функция получает список продуктов из кэша"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'product_list'
    products = cache.get(key)
    if products is None:
        products = Product.objects.all()
        cache.set(key, products)
    return products


def get_category_from_cache():
    """Функция получает список категорий из кэша"""
    if not CACHE_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    category = cache.get(key)
    if category is None:
        category = Category.objects.all()
        cache.set(key, category)
    return category
