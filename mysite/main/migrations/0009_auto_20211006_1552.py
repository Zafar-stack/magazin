# Generated by Django 3.2.5 on 2021-10-06 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_product_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Корзина', 'verbose_name_plural': 'корзина'},
        ),
        migrations.AlterModelOptions(
            name='cartitem',
            options={'verbose_name': 'Карт айтемс', 'verbose_name_plural': 'карт айтемс'},
        ),
        migrations.AlterModelOptions(
            name='podpischiki',
            options={'verbose_name': 'Подписчики', 'verbose_name_plural': 'подписчики'},
        ),
    ]
