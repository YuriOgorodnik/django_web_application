from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ProductForm, VersionForm
from .models import Product, Category, Version


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:list')
