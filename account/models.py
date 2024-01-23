from django.contrib.auth.models import AbstractUser
from django.db import models


# Create models for user.
class User(AbstractUser):
    # null = True : It means that the data stored in the corresponding table can be stored as null
    # blank = True : It means that it is mandatory to fill this field during registration
    phone_number = models.CharField(max_length=20, null=True, blank=True,  verbose_name='تلفن همراه')
    avatar = models.CharField(max_length=20, null=True, blank=True, verbose_name='تصویر آواتار')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')


    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.get_full_name()
