from django.contrib import admin
from django.http import HttpRequest
from . import models
from .models import Article


# Admin panel customization for the Article
@admin.register(models.ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'is_active']
    list_editable = ['parent', 'is_active']


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'author', 'create_date', 'is_active']
    list_editable = ['is_active']

    # Article storage time This method is called to save the author
    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)
