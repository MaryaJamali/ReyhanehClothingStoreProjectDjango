from django import forms
from .models import ContactUs


# Model_Form for Contact_us Form
class ContactUsModelForm(forms.ModelForm):
    class Meta:
        # The created form should be directly connected to the database
        model = ContactUs
        # Specify the desired model --> fields = '__all__' : Show all fields to the user
        # exclude = ['email'] : Show all fields to the user except email
        # Display fields for the user
        fields = ['full_name', 'email', 'phone_number', 'title', 'text']
        # A widget is a simple shortcode that allows you to add features to your website or blog.and we can
        # with widgets manipulate the appearance of Html forms a bit
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username@mail.com',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره موبایل(09xx-xxx-xxxx)',
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'عنوان',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام',
            }),
        }
        labels = {
            'full_name': 'نام و نام خانوادگی*',
            'email': 'ایمیل*',
            'phone_number': 'شماره موبایل*',
            'title': 'عنوان*',
            'text': 'متن پیام*',
        }
        # error_messages={} : Managing the error text
        # required : It can be used to specify that an input field in the form must be completed.
        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'
            },
            'email': {
                'required': ' فیلد ایمیل اجباری می باشد. لطفا وارد کنید'
            },
            'phone_number': {
                'required': 'شماره موبایل اجباری می باشد. لطفا وارد کنید'
            },
            'title': {
                'required': 'لطفا عنوان مورد نظرتان را وارد کنید'
            },
            'text': {
                'required': 'لطفا متن پیام مورد نظرتان را وارد کنید'
            },

        }
