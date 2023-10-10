from django.db import models


# Create your models here.
class Delivery(models.Model):
    delivery_service = models.CharField(max_length=550, verbose_name="Служба доставки")
    delivery_time = models.CharField(max_length=150, verbose_name='Срок')
    cost_of_delivery = models.CharField(max_length=100, verbose_name='Стоймость')
    delivery_country = models.TextField(verbose_name='Страны для доставки')

    def __str__(self):
        return self.delivery_service


class Payment(models.Model):
    name = models.CharField(max_length=150, verbose_name='Способ оплаты')
    descriptions = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name
