from django.db import models

from apps.movies.models import Movie


class Trailer(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE,
        related_name='trailer',
        verbose_name="Фильм",
    )
    link = models.CharField(
        max_length=600,
        verbose_name="Ссылка на трейлер",
    )

    def __str__(self):
        return f"{self.movie.title}"

    class Meta:
        verbose_name = "Трейлер"
        verbose_name_plural = "Трейлеры"
