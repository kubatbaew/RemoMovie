from django.db import models


class News(models.Model):
    title = models.CharField(
        max_length=120,
        verbose_name="Название",
    )
    poster = models.ImageField(
        upload_to='poster_news/',
        verbose_name="Постер",
    )
    description = models.TextField(
        verbose_name="Описание",
    )

    male_description = models.TextField(
        verbose_name="Маленькое описание",
    )
    image = models.ImageField(
        upload_to='news/image/',
        verbose_name="Картинка для маленького описание",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
