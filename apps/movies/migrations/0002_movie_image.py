# Generated by Django 5.0.1 on 2024-01-12 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, upload_to='movies/<function Movie.get_id at 0x7ff1b15244a0>/<function Movie.get_id at 0x7ff1b15244a0>/', verbose_name='Картинка'),
        ),
    ]