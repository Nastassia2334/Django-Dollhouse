# Generated by Django 4.1.7 on 2023-05-30 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0006_alter_delivery_cost_of_delivery_and_more'),
        ('orders', '0010_remove_orderproduct_delivery_delete_orderdelivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='order_delivery', to='delivery.delivery', verbose_name='доставка'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_type',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='delivery.payment', verbose_name='оплата'),
        ),
    ]
