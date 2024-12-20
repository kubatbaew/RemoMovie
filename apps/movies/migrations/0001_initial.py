# Generated by Django 5.0.1 on 2024-01-12 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('release_date', models.DateField(verbose_name='Даты выхода')),
                ('run_time', models.PositiveSmallIntegerField(help_text='Указывать в минутах', verbose_name='Длительность')),
                ('mpaa_rating', models.CharField(choices=[('G', 'Нет возрастных ограничений'), ('PG', 'Рекомендуется присутствие родителей'), ('PG-13', 'Детям до 13 лет просмотр не желателен'), ('R', 'Лицам до 17 лет обязательно присутствие взрослого'), ('NC-17', 'Лицам до 18 лет просмотр запрещен')], max_length=5, verbose_name='Рейтинг mpaa')),
                ('genres', models.ManyToManyField(to='genres.genre', verbose_name='Жанры')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['title'],
            },
        ),
    ]
