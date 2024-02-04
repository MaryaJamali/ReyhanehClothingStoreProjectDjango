from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView


# Class_base_Template_View for User_panel page
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel/user_panel_dashboard_page.html'


# Function_base_View for User_panel_menu
def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel/include/user_panel_menu_component.html')
