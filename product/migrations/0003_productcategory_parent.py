# Generated by Django 4.1 on 2024-01-17 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_back_image_alter_product_front_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.productcategory', verbose_name='دسته بندی والد'),
        ),
    ]
