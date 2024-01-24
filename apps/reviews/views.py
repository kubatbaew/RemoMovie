from django.shortcuts import render

from apps.reviews.models import Review
from apps.movies.models import Movie


def create_review(request, pk):
    if request.method == 'POST':
        movie = Movie.objects.get(id=pk)
