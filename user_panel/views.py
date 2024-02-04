from django.shortcuts import render
from django.views.generic import TemplateView


# Class_base_Template_View for User_panel page
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel/user_panel_dashboard_page.html'
