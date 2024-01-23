from django.db import models

from apps.movies.models import Movie
from apps.celebrities.models import Celebrity, Director

from utils.get_media_path import (
    upload_to_image_for_movie,
    upload_to_video_for_movie,

    upload_to_image_for_celebrity,
    upload_to_image_for_director
)


class MovieMediaImage(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE,
        related_name="movie_image_media",
        verbose_name="Фильм"
    )

    image = models.ImageField(
        upload_to=upload_to_image_for_movie,
        verbose_name="Картинка",
    )

    def __str__(self):
        return self.movie.title

    class Meta:
        verbose_name = "Медиа-картинка фильма"
        verbose_name_plural = "Медиа-картинки фильмов"


class MovieMediaVideo(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE,
        related_name="movie_video_media",
        verbose_name="Фильм"
    )
    video = models.FileField(
        upload_to=upload_to_video_for_movie,
        verbose_name="Видео",
    )

    def __str__(self):
        return self.movie.title

    class Meta:
        verbose_name = "Медиа-видео фильма"
        verbose_name_plural = "Медиа-видео фильмов"


class CelebrityMediaImage(models.Model):
    celebrity = models.ForeignKey(
        Celebrity, on_delete=models.CASCADE,
        related_name='celebrity_image_media',
        verbose_name="Знаменитость",
    )
    image = models.ImageField(
        upload_to=upload_to_image_for_celebrity,
        verbose_name="Картинка",
    )

    def __str__(self):
        return self.celebrity.full_name

    class Meta:
        verbose_name = "Медиа-картинка знаменитости"
        verbose_name_plural = "Медиа-картинки знаменитостей"


class DirectorMediaImage(models.Model):
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE,
        related_name='director_image_media',
        verbose_name="Режиссёр",
    )
    image = models.ImageField(
        upload_to=upload_to_image_for_director,
        verbose_name="Картинка",
    )

    def __str__(self):
        return self.director.full_name

    class Meta:
        verbose_name = "Медиа-картинка режиссёра"
        verbose_name_plural = "Медиа-картинки режиссёров"
