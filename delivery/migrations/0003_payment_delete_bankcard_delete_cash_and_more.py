# Generated by Django 4.1.7 on 2023-04-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_bankcard_cash_cashlesspayments_delete_payment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='способ оплаты')),
                ('descriptions', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.DeleteModel(
            name='BankCard',
        ),
        migrations.DeleteModel(
            name='Cash',
        ),
        migrations.DeleteModel(
            name='CashlessPayments',
        ),
    ]