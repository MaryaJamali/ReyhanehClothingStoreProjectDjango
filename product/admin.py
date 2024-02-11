from django.contrib import admin
from . import models


# Admin panel customization for the ProductCategory
@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    # Display fields on the Admin page
    list_display = ['title', 'is_active', 'is_delete']
    # Changing the fields on the Admin page
    list_editable = ['is_active']


# Admin panel customization for the ProductBrand
@admin.register(models.ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


# Admin panel customization for the ProductSize
@admin.register(models.ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


# Admin panel customization for the ProductColor
@admin.register(models.ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


# Admin panel customization for the Product
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # Filter by field in the Admin page
    list_filter = ['category', 'is_active']
    list_display = ['title', 'brand', 'size', 'color', 'price', 'is_active', 'is_delete']
    list_editable = ['is_active']


# Admin panel customization for the ProductTag
@admin.register(models.ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['caption', 'product']


# Admin panel customization for the ProductVisit
@admin.register(models.ProductVisit)
class ProductVisitAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


# Admin panel customization for the ProductWishList
@admin.register(models.ProductWishList)
class ProductWishListAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


# Admin panel customization for the ProductGallery
@admin.register(models.ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ['product']


# Admin panel customization for the ProductComment
@admin.register(models.ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'create_date', 'Score', 'parent', 'confirmation']
    list_editable = ['Score']
