from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


# Class_Form for Register Form
class RegisterForm(forms.Form):
    first_name = forms.CharField(
        label='نام *',
        # A widget is a simple shortcode that allows you to add features to your website or blog.
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'نام',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        # Using the validator, it clears the data from possible unsafe entries and converts them to standard types.
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    last_name = forms.CharField(
        label='نام خانوادگی *',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'نام خانوادگی',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    email = forms.EmailField(
        label='ایمیل *',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username@mail.com',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    phone_number = forms.CharField(
        label='شماره موبایل *',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'شماره موبایل(09xx-xxx-xxxx)',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور *',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'کلمه عبور',
                'autocomplete': 'off',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور *',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'تکرار کلمه عبور',
                'autocomplete': 'off',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


# Class_Form for Login Form
class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل *',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username@mail.com',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
    password = forms.CharField(
        label='کلمه عبور *',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'کلمه عبور',
                'autocomplete': 'off',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    remember_me = forms.BooleanField(
        label='مرا بخاطر بسپار ',
        widget=forms.CheckboxInput(
            attrs={
                'class': 'checkbox-custom-',
            }),
    )


# Class_Form for ForgotPassword Form
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل *',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username@mail.com',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )


# Class_Form for ResetPassword Form
class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='کلمه عبور *',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'کلمه عبور',
                'autocomplete': 'off',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور *',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'تکرار کلمه عبور',
                'autocomplete': 'off',
            }),
        error_messages={
            'required': 'پر کردن این فیلد الزامی است',
        },
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
