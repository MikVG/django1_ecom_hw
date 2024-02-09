import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('data_cat.json', 'r') as cat_json:
            cat = json.load(cat_json)
            return cat

    @staticmethod
    def json_read_products():
        with open('data_prod.json', 'r') as prod_json:
            prod = json.load(prod_json)
            return prod

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'],
                         description=category['fields']['description'])
            )

        Category.objects.bulk_create(category_for_create)


        for product in Command.json_read_products():
            product_for_create.append(
                Product(name=product['fields']['name'],
                        description=product['fields']['description'],
                        image=product['fields']['image'],
                        category=Category.objects.get(pk=product['fields']['category']),
                        price=product['fields']['price'])
                        )

        Product.objects.bulk_create(product_for_create)
