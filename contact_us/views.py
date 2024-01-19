from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views import View
from .forms import ContactUsModelForm


# Create your view HomePage
class ContactUsView(View):
    def get(self, request: HttpRequest):
        contact_form = ContactUsModelForm()
        return render(request, 'contact_us/contact-us.html', {
            'contact_form': contact_form
        })

    def post(self, request: HttpRequest):
        # With this command (request.POST) we have access to the data.
        # Received the data and we have access to it by contact_form
        contact_form = ContactUsModelForm(request.POST)
        # With this command, it can be checked that the information sent is correct and complete
        if contact_form.is_valid():
            phone_number = contact_form.cleaned_data['phone_number']
            if not str(phone_number).isdigit() or len(str(phone_number)) != 11:
                contact_form.add_error('phone_number', 'شماره موبایل باید 11 رقمی و  شامل اعداد باشد')
            else:
                # Save information in the database with this command
                contact_form.save()
                return redirect('home_page_view')

        return render(request, 'contact_us/contact-us.html', {
            'contact_form': contact_form
        })
