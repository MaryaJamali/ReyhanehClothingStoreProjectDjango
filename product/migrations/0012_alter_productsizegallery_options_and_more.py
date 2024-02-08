# Generated by Django 4.1 on 2024-02-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_productsizegallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsizegallery',
            options={'verbose_name': 'گالری سایز محصول', 'verbose_name_plural': 'گالری سایزهای محصول'},
        ),
        migrations.AddField(
            model_name='productsizegallery',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
        migrations.AddField(
            model_name='productsizegallery',
            name='url_title',
            field=models.CharField(db_index=True, default='', max_length=300, verbose_name='نام در url'),
        ),
    ]
