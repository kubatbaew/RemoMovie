from django.db import models


class Genre(models.Model):
    """ Модель Жанров """
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
