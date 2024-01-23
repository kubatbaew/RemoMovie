# Generated by Django 5.0.1 on 2024-01-23 08:21

import django.db.models.deletion
import utils.get_media_path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0006_remove_director_movies_director_movies'),
        ('media_people', '0008_moviemediavideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CelebrityMediaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utils.get_media_path.upload_to_image_for_celebrity, verbose_name='Картинка')),
                ('celebrity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='celebrity_image_media', to='celebrities.celebrity', verbose_name='Знаменитость')),
            ],
            options={
                'verbose_name': 'Медиа-картинка знаменитости',
                'verbose_name_plural': 'Медиа-картинки знаменитостей',
            },
        ),
        migrations.CreateModel(
            name='DirectorMediaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utils.get_media_path.upload_to_image_for_director, verbose_name='Картинка')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_image_media', to='celebrities.director', verbose_name='Режиссёр')),
            ],
            options={
                'verbose_name': 'Медиа-картинка режиссёра',
                'verbose_name_plural': 'Медиа-картинки режиссёров',
            },
        ),
    ]