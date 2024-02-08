# Generated by Django 4.1 on 2024-02-08 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_productgallery_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSizeGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.productsize', verbose_name='سایز محصول')),
            ],
            options={
                'verbose_name': 'تصویر گالری',
                'verbose_name_plural': 'گالری تصاویر',
            },
        ),
    ]
