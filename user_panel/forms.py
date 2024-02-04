from django import forms
from account.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


# Class_Form for EditProfile Form
class EditProfileModelForm(forms.ModelForm):
    class Meta:
        # The created form should be directly connected to the database
        model = User
        # Display fields for the user
        fields = ['first_name', 'last_name', 'phone_number', 'avatar', 'postal_code', 'address', 'about_user']
        # A widget is a simple shortcode that allows you to add features to your website or blog.and we can
        # with widgets manipulate the appearance of Html forms a bit
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره موبایل(09xx-xxx-xxxx)',
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'postal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'کد پستی',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'آدرس',
                'rows': 3,
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'در مورد من',
                'rows': 6,
            }),
            'current_password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'کلمه عبور فعلی',
                'rows': 6,
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'کلمه عبور',
                'rows': 6,
            }),
            'confirm_password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'تکرار کلمه عبور',
                'rows': 6,
            })
        }

        labels = {
            'first_name': 'نام *',
            'last_name': 'نام خانوادگی *',
            'phone_number': 'شماره همراه *',
            'avatar': 'تصویر پروفایل *',
            'postal_code': 'کد پستی *',
            'address': 'آدرس *',
            'about_user': 'درباره شخص *',
            'current_password': 'کلمه عبور فعلی *',
            'password': 'کلمه عبور *',
            'confirm_password': 'تکرار کلمه عبور *',
        }
        # error_messages={} : Managing the error text
        # required : It can be used to specify that an input field in the form must be completed.
        error_messages = {
            'first_name': {
                'required': 'لطفا نام خود را وارد کنید'
            },
            'last_name': {
                'required': ' لطفا نام خانوادگی خود را وارد کنید'
            },
            'phone_number': {
                'required': 'شماره موبایل اجباری می باشد. لطفا وارد کنید'
            },
            'avatar': {
                'required': 'لطفا فایل تصویر را ارسال کنید'
            },
            'postal_code': {
                'required': 'برای ارسال محصول شما است لطفا کد پستی را دقیق وارد کنید'
            },
            'address': {
                'required': 'برای ارسال محصول نیاز است لطفا آدرس را دقیق وارد کنید'
            },
            'current_password': {
                'required': 'فیلد مورد نظر اجباری می باشد. لطفا وارد کنید'
            },
            'password': {
                'required': 'فیلد مورد نظر اجباری می باشد. لطفا وارد کنید'
            },
            'confirm_password': {
                'required': 'فیلد مورد نظر اجباری می باشد. لطفا وارد کنید'
            },
        }
        validators = {
            'current_password': [
                validators.MaxLengthValidator(100),
            ],
            'password': [
                validators.MaxLengthValidator(100),
            ],
            'confirm_password': [
                validators.MaxLengthValidator(100),
            ],
            'phone_number': [RegexValidator(
                regex=r'^\d{11}$',
                message='شماره موبایل باید 11 رقمی و شامل اعداد باشد.',
                code='invalid_phone_number'
            )]
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
