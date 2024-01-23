# Generated by Django 5.0.1 on 2024-01-23 08:07

import django.db.models.deletion
import utils.get_media_path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_people', '0007_alter_moviemediaimage_image'),
        ('movies', '0007_alter_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieMediaVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=utils.get_media_path.upload_to_video_for_movie, verbose_name='Видео')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_video_media', to='movies.movie', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Медиа-видео фильма',
                'verbose_name_plural': 'Медиа-видео фильмов',
            },
        ),
    ]
