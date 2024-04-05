from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactPageView, BlogCreateView, BlogListView, \
    BlogDetailView, BlogDeleteView, BlogUpdateView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    CategoryListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('catalog/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('catalog_create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('catalog_update/<int:pk>', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('catalog_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('blog_create/', never_cache(BlogCreateView.as_view()), name='blog_create'),
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_update/<int:pk>', never_cache(BlogUpdateView.as_view()), name='blog_update'),
    path('category_list/', CategoryListView.as_view(), name='category_list')
]
