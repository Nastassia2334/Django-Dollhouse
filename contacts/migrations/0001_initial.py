# Generated by Django 4.1.7 on 2023-04-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название фирмы')),
                ('address', models.CharField(max_length=300, verbose_name='Адрес')),
                ('registration', models.TextField(verbose_name='Регистрация')),
                ('registration_number', models.TextField(verbose_name='Регистрационный номер')),
                ('mail', models.CharField(max_length=50, verbose_name='Почта')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
            ],
        ),
    ]
