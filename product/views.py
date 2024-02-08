from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Count
from utils.convertors import group_list
from utils.http_service import get_client_ip
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductBrand, ProductSize, ProductColor, ProductComment, ProductGallery, ProductVisit


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
        context['product_categories'] = (ProductCategory.objects.filter(is_active=True, is_delete=False))
        # annotate : Ability to add calculated values to an existing query set
        context['brand_categories'] = (
            ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True))
        context['size_categories'] = (
            ProductSize.objects.annotate(products_count=Count('product')).filter(is_active=True))
        context['color_categories'] = (
            ProductColor.objects.annotate(products_count=Count('product')).filter(is_active=True))
        context['product'] = query
        return context

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        brand_name = self.kwargs.get('brand')
        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)
        size_number = self.kwargs.get('size')
        if size_number is not None:
            query = query.filter(size__url_title__iexact=size_number)
        color_name = self.kwargs.get('color')
        if color_name is not None:
            query = query.filter(color__url_title__iexact=color_name)
        return query


# Class_base_List_View for ProductDetail page
class ProductDetailView(DetailView):
    template_name = 'product/product-detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        # retrieves the initial context data from the parent class of ProductDetailView.
        context = super(ProductDetailView, self).get_context_data()
        context['main_product'] = Product.objects.all()
        loaded_product = self.object
        galleries = list(ProductGallery.objects.filter(product_id=loaded_product.id).all())
        galleries.insert(0, loaded_product)
        context['product_galleries_group'] = group_list(galleries, 6)
        context['related_products'] = group_list(list(Product.objects.filter(brand_id=loaded_product.brand_id).exclude
                                                      (pk=loaded_product.id).all()[:12]), 4)
        # Object is the key of the product value
        product: Product = kwargs.get('object')
        # This code shows us that when the parent is None, it is the original comment, not the reply
        # prefetch_related : To avoid additional queries and retrieve information with one query
        context['comments'] = (ProductComment.objects.filter(product_id=product.id, parent=None, confirmation=True).order_by
                               ('-create_date').prefetch_related('productcomment_set'))
        context['comments_count'] = ProductComment.objects.filter(product_id=product.id, confirmation=True).count()
        # Obtaining the user's IP address and ID in the database
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        # Checking whether the user has already seen the product with his IP or not
        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id)
            new_visit.save()
        return context


# Function_base_View for add_product_comment page
def add_product_comment(request: HttpRequest):
    if request.user.is_authenticated:
        product_id = request.GET.get('product_id')
        product_comment = request.GET.get('product_comment')
        parent_id = request.GET.get('parent_id')
        # Fill in the desired fields and save
        new_comment = ProductComment(product_id=product_id, text=product_comment,
                                     user_id=request.user.id, parent_id=parent_id)
        new_comment.save()
        context = {
            'comments': ProductComment.objects.filter(product_id=product_id, parent=None, confirmation=True).order_by(
                '-create_date').prefetch_related('productcomment_set'),
            'comments_count': ProductComment.objects.filter(product_id=product_id, confirmation=True).count(),
        }
        return render(request, 'product/include/product-comments-component.html', context=context)
    return HttpResponse('response')
