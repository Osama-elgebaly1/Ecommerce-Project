# Generated by Django 5.0.3 on 2025-04-24 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce_Core', '0007_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
