# Generated by Django 4.1 on 2024-02-21 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0006_sitesetting_header_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionCommonGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی سوالات متداول',
                'verbose_name_plural': 'دسته بندی های سوالات متداول',
            },
        ),
        migrations.CreateModel(
            name='QuestionCommon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='سوال')),
                ('response', models.URLField(max_length=500, verbose_name='پاسخ')),
                ('question_common_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_setting.questioncommongroup', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'سوال متداول',
                'verbose_name_plural': 'سوالات متداول',
            },
        ),
    ]
