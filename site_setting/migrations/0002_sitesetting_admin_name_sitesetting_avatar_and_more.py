# Generated by Django 4.1 on 2024-01-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetting',
            name='admin_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام ادمین'),
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/site-setting', verbose_name='تصویر ادمین'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='site_logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/site-setting', verbose_name='لوگو سایت'),
        ),
    ]
