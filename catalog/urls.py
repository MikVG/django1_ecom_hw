from django.urls import path

from catalog.views import home, contacts, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>', product_detail, name='product')
]
