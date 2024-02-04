from django.contrib.auth.models import AbstractUser
from django.db import models


# Create models for user.
class User(AbstractUser):
    # null = True : It means that the data stored in the corresponding table can be stored as null
    # blank = True : It means that it is mandatory to fill this field during registration
    phone_number = models.CharField(max_length=20, null=True, blank=True,  verbose_name='تلفن همراه')
    avatar = models.ImageField(upload_to='images/avatar', null=True, blank=True, verbose_name='تصویر آواتار')
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعالسازی ایمیل')
    about_user = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    postal_code = models.CharField(max_length=20, null=True, blank=True,  verbose_name='کد پستی')
    address = models.TextField(null=True, blank=True, verbose_name='آدرس')

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()

        return self.email

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
