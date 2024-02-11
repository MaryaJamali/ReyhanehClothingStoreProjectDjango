from django.db import models
from django.urls import reverse
from account.models import User


# Create models for Product.
class ProductCategory(models.Model):
    # db_index = True : It goes back to the way of retrieving information....
    # ...This increases the speed of query and is used for fields that receive a lot of query.
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')
    # The information is not displayed except in the admin
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='نام برند')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='نام در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class ProductSize(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='سایز')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='نام در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز ها'


class ProductColor(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='نام رنگ')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='نام در url')
    is_active = models.BooleanField(verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    # related_name : To retrieve the information of the main Django command (classname_set --> product_set),
    # we change the name of the command with this tag. (instead of product_set --> product_categories)
    # Examining the many-to-many relationship in tables with (models.ManyToManyField)
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='دسته بندی ها')
    # null = True : Django stores empty values as NULL in the database for fields where appropriate
    # blank = True : It is  mandatory to fill the field
    front_image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر جلوی محصول')
    back_image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر پشت محصول')
    # on_delete = models.CASCADE : The category has been deleted, the information of this section should also be deleted
    # Check one-to-many relationship in tables with (models.ForeignKey)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True, blank=True, verbose_name='برند')
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE, null=True, blank=True, verbose_name='سایز')
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, null=True, blank=True, verbose_name='رنگ')
    price = models.IntegerField(verbose_name='قیمت محصول')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(db_index=True, verbose_name='توضیحات اصلی')
    # Slug is the dynamic and changeable part ---> Domain name/posts/slug (for example : samsung s20 --> samsung-s-20)
    # unique = True : If there is a duplicate state, it changes the state to be unique
    slug = models.SlugField(max_length=200, default="", null=False, db_index=True, blank=True, unique=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-detail_page_view', args=[self.slug])

    # Overwriting the save command
    def save(self, *args, **kwargs):
        # Converts the title to a slug ----> self.slug = slugify(self.title)
        # With this command, we want the core of Django not to be changed in the case of Save
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'


class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول')
    ip = models.CharField(max_length=30, verbose_name='آی پی کاربر')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='کاربر')

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدیدهای محصول'


class ProductWishList(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'محصول مورد علاقه'
        verbose_name_plural = 'محصولات مورد علاقه'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(upload_to='images/product_gallery', verbose_name='تصویر')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'گالری تصاویر'


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    parent = models.ForeignKey('ProductComment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')
    Score = models.IntegerField(default=1, verbose_name='امتیاز به محصول')
    confirmation = models.BooleanField(default=True, verbose_name='تایید شده/نشده')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر محصول'
        verbose_name_plural = 'نظرات محصول'
