from types import NoneType

from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from apps.movies.models import Movie
from apps.genres.models import Genre


class MovieListView(generic.ListView):
    model = Movie
    template_name = 'pages/movies/movielist.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.GET.get('title')
        genres = self.request.GET.getlist('genres')
        mppa_rating = self.request.GET.get('mppa_rating')

        if title:
            queryset = queryset.filter(Q(title__icontains=title))

        if genres:
            queryset = queryset.filter(genres__title__in=genres)

        if mppa_rating:
            queryset = queryset.filter(mpaa_rating=mppa_rating)

        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['genres'] = Genre.objects.all()
        context['count_movie'] = self.get_queryset().count()
        context['rating_all'] = [rating for rating in Movie.MPAARating.choices]

        paginator = Paginator(context['movie_list'], self.paginate_by)
        page = self.request.GET.get('page')

        try:
            context['movie_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['movie_list'] = paginator.page(1)
        except EmptyPage:
            context['movie_list'] = paginator.page(paginator.num_pages)

        return context


class MovieGridListView(generic.ListView):
    model = Movie
    template_name = "pages/movies/moviegrid.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['genres'] = Genre.objects.all()
        context['count_movie'] = self.get_queryset().count()
        context['rating_all'] = [rating for rating in Movie.MPAARating.choices]

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        title = self.request.GET.get('title')
        genres = self.request.GET.getlist('genres')
        mppa_rating = self.request.GET.get('mppa_rating')

        if title:
            queryset = queryset.filter(Q(title__icontains=title))

        if genres:
            queryset = queryset.filter(genres__title__in=genres)

        if mppa_rating:
            queryset = queryset.filter(mpaa_rating=mppa_rating)

        return queryset


class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = "pages/movies/moviesingle.html"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie = self.get_object()

        context['related_movies'] = Movie.objects.all().filter(genres__in=movie.genres.all()).exclude(id=movie.id).distinct()

        appraisal = []

        for review in movie.reviews.all():
            for i in range(review.appraisal):
                appraisal.append(1)

        appraisal_default = [i for i in range(10 - len(appraisal))]

        context['appraisal'] = appraisal
        context['appraisal_default'] = appraisal_default

        return context
