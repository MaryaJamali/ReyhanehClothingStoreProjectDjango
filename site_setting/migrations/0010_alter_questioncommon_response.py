# Generated by Django 4.1 on 2024-02-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0009_remove_questioncommon_question_common_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questioncommon',
            name='response',
            field=models.TextField(verbose_name='پاسخ'),
        ),
    ]