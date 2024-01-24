from django.views import generic

from apps.news.models import News


class NewsDetailView(generic.DetailView):
    model = News
    pk_url_kwarg = 'pk'
    template_name = 'pages/news/blogsingle.html'
