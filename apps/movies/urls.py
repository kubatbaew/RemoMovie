from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from apps.movies.views import MovieListView, MovieGridListView, MovieDetailView


urlpatterns = [
    path('movies-list/', MovieListView.as_view(), name="movies_list"),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name="movie_detail"),
    path('movies-grid/', MovieGridListView.as_view(), name="movies_grid"),
]
