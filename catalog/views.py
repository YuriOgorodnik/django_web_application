from gettext import Catalog

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, Category


# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'Товары нашего магазина'
#     }
#     return render(request, 'catalog/product_list.html', context)


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Товары нашего магазина'
    }


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductDetailView(DetailView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        product = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        context_data['category_pk'] = product.pk
        context_data['title'] = 'Информация о товаре'
        context_data['object_list'] = Product.objects.filter(id=self.kwargs.get('pk'))
        context_data['description'] = product.description
        return context_data
