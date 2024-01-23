from django.db import models


# Create models for site_setting.
class SiteSetting(models.Model):
    admin_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='نام ادمین')
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    site_url = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='شماره تلفن')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='شماره فکس')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.TextField(verbose_name='متن کپی رایت سایت')
    about_us_text = models.TextField(verbose_name='متن درباره ما سایت')
    site_logo = models.ImageField(upload_to='images/site-setting', null=True, blank=True, verbose_name='لوگو سایت')
    avatar = models.ImageField(upload_to='images/site-setting', null=True, blank=True, verbose_name='تصویر ادمین')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'


class MenuLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='نام منو')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی اصلی منو'
        verbose_name_plural = 'دسته بندی های اصلی منو'


class MenuLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    menu_link_box = models.ForeignKey(to=MenuLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لینک منو'
        verbose_name_plural = 'لینک های منو'


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=1000, verbose_name='لینک')
    url_title = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.CharField(max_length=600, verbose_name='توضیحات اسلایدر')
    slider_image = models.ImageField(upload_to='images/sliders', null=True, blank=True, verbose_name='تصویر اسلایدر')
    display_order = models.IntegerField(verbose_name='اولویت نمایش')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'لینک فوتر'
        verbose_name_plural = 'لینک های فوتر'
