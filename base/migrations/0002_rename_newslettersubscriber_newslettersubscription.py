# Generated by Django 4.1 on 2024-02-10 12:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewsletterSubscriber',
            new_name='NewsletterSubscription',
        ),
    ]
