from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

from apps.movies.models import Movie

User = get_user_model()


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='reviews_user',
        verbose_name="Пользователь"
    )
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name="Фильм",
    )
    object = models.CharField(
        max_length=120,
        verbose_name="Тема",
    )
    appraisal = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10),
        ],
        verbose_name="Оценка",
    )
    text = models.TextField(
        max_length=300,
        verbose_name="Текст",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
    )

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['created_at']
