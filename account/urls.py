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
    path('register/', views.RegisterView.as_view(), name='register_page_view'),
    path('login/', views.LoginView.as_view(), name='login_page_view'),
    path('logout/', views.LogoutView.as_view(), name='logout_page_view'),
    path('forget-password/', views.ForgetPasswordView.as_view(), name='forget_password_page_view'),
    path('reset-password/<active_code>', views.ResetPasswordView.as_view(), name='reset_password_page_view'),
    path('activate-account/<email_active_code>', views.ActivateAccountView.as_view(), name='activate_account_view'),
]
