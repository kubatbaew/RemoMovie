# Generated by Django 5.0.1 on 2024-01-12 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.ImageField(upload_to='movies/<django.db.models.fields.CharField>/', verbose_name='Картинка'),
        ),
    ]