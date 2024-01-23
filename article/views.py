from django.views.generic.list import ListView
from article.models import Article


# Class_base_View for Articles page
class ArticlesListView(ListView):
    model = Article
    paginate_by = 6
    template_name = 'article/article-list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticlesListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = super(ArticlesListView, self).get_queryset()
        query = query.filter(is_active=True)
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(selected_categories__url_title__iexact=category_name)
        return query