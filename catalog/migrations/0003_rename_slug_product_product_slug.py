# Generated by Django 4.1.7 on 2023-04-01 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_colorall_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='slug',
            new_name='product_slug',
        ),
    ]