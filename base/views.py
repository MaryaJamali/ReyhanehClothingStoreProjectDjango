from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic.base import TemplateView
from site_setting.models import Slider, SiteSetting, FooterLinkBox


# Class_base_templateview for Home page
class HomeView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        slider = Slider.objects.filter(is_active=True)
        context['sliders'] = slider
        return context


# Class_base_templateview for AboutUs page
class AboutUsView(TemplateView):
    template_name = 'base/about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context


# Class_base_templateview for AboutUs page
class Error404View(TemplateView):
    template_name = 'shared/404.html'


# Function_base_view for site-header-component page
def site_header_component(request: HttpRequest):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site-header-component.html', context=context)


# Function_base_view for site-customer-features-component page
def site_customer_features_component(request: HttpRequest):
    return render(request, 'shared/site-customer-features-component.html')


# Function_base_view for site-footer-component page
def site_footer_component(request: HttpRequest):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        # It refers to the set of category links
        item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes
    }
    return render(request, 'shared/site-footer-component.html', context=context)
