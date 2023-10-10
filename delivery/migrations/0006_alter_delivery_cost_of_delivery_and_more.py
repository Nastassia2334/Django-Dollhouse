# Generated by Django 4.1.7 on 2023-05-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_remove_payment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='cost_of_delivery',
            field=models.CharField(max_length=100, verbose_name='Стоймость'),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_country',
            field=models.TextField(verbose_name='Страны для доставки'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Способ оплаты'),
        ),
    ]
