# Generated by Django 5.0.1 on 2024-01-18 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movies/<django.db.models.fields.CharField>/', verbose_name='Картинка'),
        ),
    ]
