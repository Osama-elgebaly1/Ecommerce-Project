# Generated by Django 5.0.3 on 2025-04-18 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_Core', '0002_alter_product_image_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_after_discount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
