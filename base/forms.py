from django import forms
from django.core import validators


# Class_Form for NewsletterSubscriber Form
class NewsletterSubscriberForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل *',
        # A widget is a simple shortcode that allows you to add features to your website or blog.and we can
        # with widgets manipulate the appearance of Html forms a bit
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'username@mail.com',
            }),
        error_messages={
            'required': 'لطفا ایمیل خود را وارد کنید',
        },
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )
