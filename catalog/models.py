from datetime import datetime

from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=250, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='изображение', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    date_creation = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    date_last_modified = models.DateTimeField(verbose_name='дата последнего изменения', auto_now=True)

    def __str__(self):
        return (f'{self.name} {self.description} {self.category} {self.price} {self.date_creation} '
                f'{self.date_last_modified}')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
