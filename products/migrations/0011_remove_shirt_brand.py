# Generated by Django 4.2.2 on 2023-06-11 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirt',
            name='brand',
        ),
    ]