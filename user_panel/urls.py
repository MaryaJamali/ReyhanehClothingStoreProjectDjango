"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelDashboardPage.as_view(), name='user_panel_dashboard_page_view'),
    path('edit-profile/', views.EditUserProfilePage.as_view(), name='edit_profile_page_view'),
    path('change-pass/', views.ChangePasswordPage.as_view(), name='change_password_page_view'),
    path('user-cart', views.user_basket, name='user_basket_page_view'),
    path('my-shopping/', views.MyShopping.as_view(), name='user_shopping_page_view'),
    path('my-shopping-detail/<order_id>', views.my_shopping_detail, name='user_shopping_detail_page_view'),
    path('remove-cart-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-cart-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),
]
