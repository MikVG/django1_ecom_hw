from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactPageView(TemplateView):
    template_name = 'catalog/contacts.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('catalog:blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('catalog:blog_list')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog_list')
