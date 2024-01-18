from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic.base import TemplateView


# Class_base_templateview for Home page
class HomeView(TemplateView):
    template_name = 'base/index.html'


# Class_base_templateview for AboutUs page
class AboutUsView(TemplateView):
    template_name = 'base/about-us.html'


# Class_base_templateview for AboutUs page
class Error404View(TemplateView):
    template_name = 'shared/404.html'


# Function_base_view for site-header-component page
def site_header_component(request: HttpRequest):
    return render(request, 'shared/site-header-component.html')


# Function_base_view for site-customer-features-component page
def site_customer_features_component(request: HttpRequest):
    return render(request, 'shared/site-customer-features-component.html')


# Function_base_view for site-footer-component page
def site_footer_component(request: HttpRequest):
    return render(request, 'shared/site-footer-component.html')
