from django.db import models


# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    phone_number = models.IntegerField(null=True, blank=True, verbose_name='شماره موبایل')
    text = models.TextField(verbose_name='متن تماس با ما')
    # auto_now_add = True : When registering, the date is automatically updated and recorded
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    # null = True : Django stores empty values as NULL in the database for fields where appropriate
    # blank = True : It is  mandatory to fill the field
    response = models.TextField(null=True, blank=True, verbose_name='متن پاسخ تماس با ما')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'
