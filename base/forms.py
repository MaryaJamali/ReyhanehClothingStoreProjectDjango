from django import forms
from django.core import validators
from .models import NewsletterSubscription


# Class_Form for NewsletterSubscription Form
class NewsletterSubscriptionModelForm(forms.ModelForm):
    class Meta:
        # The created form should be directly connected to the database
        model = NewsletterSubscription
        # Display fields for the user
        fields = ['email']
        # A widget is a simple shortcode that allows you to add features to your website or blog.and we can
        # with widgets manipulate the appearance of Html forms a bit
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'لطفا ایمیل خود را وارد کنید'
            }),
        }
        labels = {
            'email': 'ایمیل*',
        }
        # error_messages={} : Managing the error text
        # required : It can be used to specify that an input field in the form must be completed.
        error_messages = {
            'email': {
                'required': 'لطفا ایمیل خود را وارد کنید'
            },
        }
        validators = [
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
