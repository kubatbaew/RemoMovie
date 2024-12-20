# Generated by Django 5.0.1 on 2024-01-18 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0002_celebrity_image'),
        ('movies', '0007_alter_movie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='celebrity/', verbose_name='Картинка')),
                ('full_name', models.CharField(max_length=120, verbose_name='Полное имя')),
                ('bio', models.TextField(verbose_name='Биография')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('height', models.IntegerField(help_text='Указать в сантиметрах', verbose_name='Рост')),
                ('facebook', models.URLField(verbose_name='Фейсбук')),
                ('twitter', models.URLField(verbose_name='Твиттер')),
                ('gmail', models.URLField(verbose_name='Почта')),
                ('linkedin', models.URLField(verbose_name='Линкедин')),
                ('movies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director', to='movies.movie', verbose_name='Фильмы которые снимал')),
            ],
            options={
                'verbose_name': 'Знаменитость',
                'verbose_name_plural': 'Знаменитости',
                'ordering': ['full_name'],
            },
        ),
    ]
