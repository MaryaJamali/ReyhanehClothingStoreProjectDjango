# Generated by Django 4.1 on 2024-01-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0002_sitesetting_admin_name_sitesetting_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال / غیرفعال'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=models.CharField(max_length=600, verbose_name='توضیحات اسلایدر'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.URLField(max_length=1000, verbose_name='لینک'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url_title',
            field=models.CharField(max_length=200, verbose_name='عنوان لینک'),
        ),
    ]
