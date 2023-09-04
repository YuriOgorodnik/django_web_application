from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category1 = Category.objects.create(name='Электроника')
        category2 = Category.objects.create(name='Компьютеры')
        category3 = Category.objects.create(name='Бытовая техника')

        Product.objects.create(
            name='Мобильный телефон',
            description='Смартфон Apple iPhone 14 128GB',
            category=category1,
            price=2699
        )
        Product.objects.create(
            name='Ноутбук',
            description='Ноутбук Apple Macbook Air 13 M1 2020 MGN63',
            category=category2,
            price=3090
        )
        Product.objects.create(
            name='Холодильник',
            description='Холодильник Samsung RB37A52N0B1/WT',
            category=category3,
            price=2899
        )

        self.stdout.write(self.style.SUCCESS('Данные успешно добавлены.'))
