# Generated by Django 4.1 on 2024-01-23 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0003_slider_is_active_alter_slider_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='نام منو')),
                ('url', models.URLField(blank=True, max_length=500, null=True, verbose_name='لینک')),
            ],
            options={
                'verbose_name': 'دسته بندی اصلی منو',
                'verbose_name_plural': 'دسته بندی های اصلی منو',
            },
        ),
        migrations.CreateModel(
            name='MenuLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('menu_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_setting.menulinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک منو',
                'verbose_name_plural': 'لینک های منو',
            },
        ),
    ]
