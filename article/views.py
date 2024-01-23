from django.views.generic.list import ListView
from django.views.generic import DetailView
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
        return query


# Class_base_View for ArticleDetail page
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article/article-detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        return context

    def get_queryset(self):
        query = super(ArticleDetailView, self).get_queryset()
        query = query.filter(is_active=True)
        return query
