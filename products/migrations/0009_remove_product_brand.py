# Generated by Django 4.2.2 on 2023-06-11 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
    ]
