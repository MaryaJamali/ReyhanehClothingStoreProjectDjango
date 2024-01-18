from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory


# Class_base_List_View for Product page
class ProductListView(ListView):
    template_name = 'product/product-list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 8

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        context['main_categories'] = ProductCategory.objects.filter(is_active=True, parent_id=None)
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['product'] = query
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        return query


# Class_base_List_View for Product page
class ProductDetailView(DetailView):
    template_name = 'product/product-detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get("product_favorites")
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context
