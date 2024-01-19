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
            # Save information in the database with this command
            contact_form.save()
            return redirect('home_page_view')

        return render(request, 'contact_us/contact-us.html', {
            'contact_form': contact_form
        })
