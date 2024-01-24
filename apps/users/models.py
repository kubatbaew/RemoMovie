from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.movies.models import Movie


class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="users/avatar/",
        verbose_name="Аватар",
    )
    favorite_movies = models.ManyToManyField(
        Movie,
        blank=True,
        verbose_name="Фильмы",
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
