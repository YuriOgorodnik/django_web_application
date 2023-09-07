from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(verbose_name='цена', max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата последнего изменения', auto_now=True)

    def __str__(self):
        return (f'{self.name} {self.description} {self.category} {self.price} {self.created_at} '
                f'{self.updated_at}')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
