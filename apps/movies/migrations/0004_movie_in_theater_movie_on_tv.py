# Generated by Django 5.0.1 on 2024-01-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='in_theater',
            field=models.BooleanField(default=False, verbose_name='В театре'),
        ),
        migrations.AddField(
            model_name='movie',
            name='on_tv',
            field=models.BooleanField(default=False, verbose_name='На телевидении'),
        ),
    ]
