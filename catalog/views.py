from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'name: {name}\n'
              f'phone: {phone}\n'
              f'message: {message}')

    return render(request, 'catalog/contacts.html')
