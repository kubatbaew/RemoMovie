from django.db import models

from apps.movies.models import Movie


class Celebrity(models.Model):
    """ Модель Знаменитости """

    image = models.ImageField(
        upload_to="celebrity/",
        verbose_name="Картинка",
        blank=True,
        null=True,
    )
    full_name = models.CharField(
        max_length=120,
        verbose_name="Полное имя",
    )
    prof = models.CharField(
        max_length=120,
        verbose_name="Профессия",
    )
    bio = models.TextField(
        verbose_name="Биография",
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
    )
    height = models.IntegerField(
        verbose_name="Рост",
        help_text="Указать в сантиметрах",
    )
    movies = models.ManyToManyField(
        Movie,
        verbose_name="Фильмы в котором снимался",
        related_name="celebrity",
        blank=True,
    )

    # Social Links
    facebook = models.URLField(verbose_name="Фейсбук")
    twitter = models.URLField(verbose_name="Твиттер")
    gmail = models.URLField(verbose_name="Почта")
    linkedin = models.URLField(verbose_name="Линкедин")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Знаменитость"
        verbose_name_plural = "Знаменитости"
        ordering = ['full_name']


class Director(models.Model):
    """ Модель Режиссёров """

    image = models.ImageField(
        upload_to="celebrity/",
        verbose_name="Картинка",
        blank=True,
        null=True,
    )
    full_name = models.CharField(
        max_length=120,
        verbose_name="Полное имя",
    )
    bio = models.TextField(
        verbose_name="Биография",
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения",
    )
    country = models.CharField(
        max_length=50,
        verbose_name="Страна",
    )
    movies = models.ManyToManyField(
        Movie,
        verbose_name="Фильмы которые снимал",
        related_name="director",
    )

    # Social Links
    facebook = models.URLField(verbose_name="Фейсбук")
    twitter = models.URLField(verbose_name="Твиттер")
    gmail = models.URLField(verbose_name="Почта")
    linkedin = models.URLField(verbose_name="Линкедин")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"
        ordering = ['full_name']
