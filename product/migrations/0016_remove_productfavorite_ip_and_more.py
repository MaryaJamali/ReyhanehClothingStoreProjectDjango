# Generated by Django 4.1 on 2024-02-10 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_productfavorite_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfavorite',
            name='ip',
        ),
        migrations.AlterField(
            model_name='productfavorite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='نام محصول'),
        ),
    ]