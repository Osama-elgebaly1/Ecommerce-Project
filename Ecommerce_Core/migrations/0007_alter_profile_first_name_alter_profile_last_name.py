# Generated by Django 5.0.3 on 2025-04-24 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_Core', '0006_alter_profile_address_alter_profile_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
