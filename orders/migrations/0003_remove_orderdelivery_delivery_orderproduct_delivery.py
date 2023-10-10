# Generated by Django 4.1.7 on 2023-05-30 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderdelivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdelivery',
            name='delivery',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='delivery',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='orders.orderdelivery', verbose_name='доставка'),
            preserve_default=False,
        ),
    ]