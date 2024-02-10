from django.db import models
from account.models import User


# Create models for NewsletterSubscription.
class NewsletterSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    email = models.EmailField(unique=True, max_length=300, verbose_name='ایمیل')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'ایمیل اشتراک در خبرنامه'
        verbose_name_plural = 'ایمیل های اشتراک در خبرنامه'
