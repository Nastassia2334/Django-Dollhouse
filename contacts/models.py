from django.db import models


# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название фирмы')
    address = models.CharField(max_length=300, verbose_name='Адрес')
    registration = models.TextField(verbose_name='Регистрация')
    registration_number = models.TextField(verbose_name='Регистрационный номер')
    mail = models.CharField(max_length=50, verbose_name='Почта')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    working_mode = models.TextField(verbose_name='Режим работы', blank=True)



