from gettext import Catalog

from django.shortcuts import render
from .models import Product, Category


def home(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Товары нашего магазина'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def show_product(request, pk):
    product = Category.objects.get(pk=pk)
    product_description = product.description
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': 'Информация о товаре',
        'description': product_description
    }
    return render(request, 'catalog/product.html', context)
