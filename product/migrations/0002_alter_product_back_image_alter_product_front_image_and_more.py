# Generated by Django 4.1 on 2024-01-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='back_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر پشت محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='front_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر جلوی محصول'),
        ),
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(upload_to='images/product_gallery', verbose_name='تصویر'),
        ),
    ]
