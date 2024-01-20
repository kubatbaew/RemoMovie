from django.db import models

from apps.genres.models import Genre


class Movie(models.Model):
    """ Модель фильмов """

    class MPAARating(models.TextChoices):
        G = 'G', 'Нет возрастных ограничений'
        PG = 'PG', 'Рекомендуется присутствие родителей'
        PG13 = 'PG-13', 'Детям до 13 лет просмотр не желателен'
        R = 'R', 'Лицам до 17 лет обязательно присутствие взрослого'
        NC17 = 'NC-17', 'Лицам до 18 лет просмотр запрещен'

    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        upload_to="movies/",
        verbose_name="Картинка",
        null=True,
        blank=True,
    )
    genres = models.ManyToManyField(
        Genre,
        verbose_name="Жанры",
    )
    release_date = models.DateField(
        verbose_name="Даты выхода",
    )
    run_time = models.PositiveSmallIntegerField(
        verbose_name="Длительность",
        help_text="Указывать в минутах",
    )
    mpaa_rating = models.CharField(
        max_length=5,
        choices=MPAARating.choices,
        verbose_name="Рейтинг mpaa",
    )
    in_theater = models.BooleanField(
        default=False,
        verbose_name="В театре",
    )
    on_tv = models.BooleanField(
        default=False,
        verbose_name="На телевидении",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['title']
