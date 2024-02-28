from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactPageView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('catalog/<int:pk>', ProductDetailView.as_view(), name='product')
]
