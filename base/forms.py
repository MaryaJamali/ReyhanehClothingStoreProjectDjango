from django import forms
from .models import NewsletterSubscriber


# Class_Form for NewsletterSubscriber Form
class NewsletterSubscriberModelForm(forms.ModelForm):
    class Meta:
        # The created form should be directly connected to the database
        model = NewsletterSubscriber
        # Display fields for the user
        fields = ['email']
        # A widget is a simple shortcode that allows you to add features to your website or blog.and we can
        # with widgets manipulate the appearance of Html forms a bit
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username@mail.com'
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
