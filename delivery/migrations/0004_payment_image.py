# Generated by Django 4.1.7 on 2023-04-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_payment_delete_bankcard_delete_cash_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='image',
            field=models.FileField(blank=True, upload_to='image/'),
        ),
    ]