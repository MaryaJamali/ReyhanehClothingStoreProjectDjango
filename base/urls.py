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
    path('', views.HomeView.as_view(), name='home_page_view'),
    path('about-us', views.AboutUsView.as_view(), name='about_us_page_view'),
    path('question-common', views.question_common_view, name='question_common_page_view'),
    path('cooperation', views.Cooperation.as_view(), name='cooperation_page_view'),
    path('size-guide', views.SizeGuide.as_view(), name='size-guide_page_view'),
    path('404', views.Error404View.as_view(), name='error_404_page_view'),
    # Addressing example for component pages
    path('subscribe/', views.site_footer_component, name='site_footer_component_view'),
]
