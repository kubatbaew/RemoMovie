from django.shortcuts import render

from django.http import HttpRequest

from apps.movies.models import Movie
from apps.celebrities.models import Celebrity
from apps.trailers.models import Trailer


def homepage(request: HttpRequest):
    movies = Movie.objects.all()

    in_theater = Movie.objects.filter(in_theater=True)
    on_tv = Movie.objects.filter(on_tv=True)

    celebrities = Celebrity.objects.all()[:4]

    trailers = Trailer.objects.all()

    return render(request, 'pages/homepage/index.html', locals())
