# Generated by Django 5.0.1 on 2024-01-22 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_people', '0004_alter_moviemediaimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemediaimage',
            name='image',
            field=models.ImageField(upload_to='<classmethod(<function MovieMediaImage.get_instance at 0x000002A7B4178F40>)>/media/image', verbose_name='Картинка'),
        ),
    ]
