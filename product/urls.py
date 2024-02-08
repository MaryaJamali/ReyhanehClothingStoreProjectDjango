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
    path('', views.ProductListView.as_view(), name='product_list_page_view'),
    path('cat/<str:category>', views.ProductListView.as_view(), name='product_list_by_category'),
    path('brand/<str:brand>', views.ProductListView.as_view(), name='product_list_by_brands'),
    path('size/<int:size>', views.ProductListView.as_view(), name='product_list_by_size'),
    # Slug is the dynamic and changeable part ---> Domain name/posts/slug
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail_page_view'),
    path('add-product-comment', views.add_product_comment, name='add_product_comment')
]
