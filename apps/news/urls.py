from django.urls import path

from apps.news.views import NewsDetailView


urlpatterns = [
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
]
