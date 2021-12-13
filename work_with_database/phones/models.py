from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=70, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    images = models.ImageField(null=True, verbose_name='Изображения')
    release_date = models.DateField(auto_now_add=False, verbose_name='Дата')
    lte_exists = models.BooleanField(null=True)
    slug = models.SlugField(max_length=255, verbose_name='URL')

    def __str__(self):
        return self.name
