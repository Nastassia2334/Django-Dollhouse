from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категория")
    category_slug = models.SlugField(max_length=30, unique=True)
    image = models.FileField(upload_to="image/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_slug', args=[str(self.category_slug)])


class Product(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Название")
    product_slug = models.SlugField(max_length=70, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Цена")
    options = models.CharField(max_length=500, verbose_name="Параметры")
    weight = models.CharField(max_length=50, blank=True, verbose_name="Вес")
    material = models.CharField(max_length=400, verbose_name="Материал")
    coverage = models.CharField(max_length=400, blank=True, verbose_name="Покрытие")
    equipment = models.CharField(max_length=1000, blank=True, verbose_name="Комплектация")
    # описание
    description = models.TextField(verbose_name="Описание")
    # картинка
    image = models.FileField(upload_to="image/", blank=True, verbose_name="Фото")
    color = models.ForeignKey('Colors', default=1, on_delete=models.CASCADE, verbose_name="Цвет")

    def __str__(self):
        return self.name

    def get_object(self, *args, **kwargs):
        return reverse('product_slug', args=[str(self.product_slug)])


class Gallery(models.Model):
    image = models.FileField(upload_to="image/")
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name


class Colors(models.Model):
    colors_product = models.CharField(max_length=100, verbose_name="Цвет")

    def __str__(self):
        return self.colors_product
