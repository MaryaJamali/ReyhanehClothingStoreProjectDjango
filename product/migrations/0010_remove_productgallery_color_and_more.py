# Generated by Django 4.1 on 2024-02-08 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_productgallery_color_productgallery_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productgallery',
            name='color',
        ),
        migrations.RemoveField(
            model_name='productgallery',
            name='size',
        ),
    ]
