from django.db import models
from catalog.models import Product
from delivery.models import Delivery, Payment



# Create your models here.
class Order(models.Model):
    # данные покупателя
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='@mail')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    address = models.CharField(max_length=250, verbose_name='Улица, дом, квартира')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    delivery_type = models.ForeignKey(Delivery, related_name='order_delivery', on_delete=models.CASCADE, verbose_name='доставка', blank=True, default='')
    payment_type = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name='оплата', blank=True, default='')

    def __str__(self):
        return f'номер {self.id}'


class OrderProduct(models.Model):
    # данные о заказе
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE, verbose_name='заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='продукт')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')


    def __str__(self):
        return f'номер {self.id}'



