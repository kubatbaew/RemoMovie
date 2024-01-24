from django.db import models

from apps.news.models import News
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_comments",
        verbose_name="Пользователь",
    )
    news = models.ForeignKey(
        News, on_delete=models.CASCADE,
        related_name='news_comments',
        verbose_name="Новость",
    )
    text = models.TextField(
        max_length=300,
        verbose_name="Текст",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание",
    )

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
