from datetime import datetime

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='заголовок')
    slug = models.CharField(max_length=250, verbose_name='слаг')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blogs/', verbose_name='изображение', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='дата создания', default=datetime.now)
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return (f'{self.title} {self.slug} {self.content}')

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
