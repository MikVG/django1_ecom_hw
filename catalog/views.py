from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    """
    функция выдает страницу со всеми продуктами
    """
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/home.html',  context)


def product_detail(request, pk):
    """
    функция выдает страницу с одним продуктом
    """
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html',  context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'name: {name}\n'
              f'phone: {phone}\n'
              f'message: {message}')

    return render(request, 'catalog/contacts.html')
