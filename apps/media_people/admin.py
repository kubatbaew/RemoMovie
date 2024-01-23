from django.contrib import admin

from apps.media_people.models import (
    MovieMediaImage,
    MovieMediaVideo,

    CelebrityMediaImage,
    DirectorMediaImage,
)


@admin.register(MovieMediaImage)
class MovieMediaImageAdmin(admin.ModelAdmin):
    list_display = ['movie']
    search_fields = ['movie']
    ordering = ['movie']


@admin.register(MovieMediaVideo)
class MovieMediaVideoAdmin(admin.ModelAdmin):
    list_display = ['movie']
    search_fields = ['movie']
    ordering = ['movie']


@admin.register(CelebrityMediaImage)
class CelebrityMediaImageAdmin(admin.ModelAdmin):
    list_display = ['celebrity']
    search_fields = ['celebrity']
    ordering = ['celebrity']


@admin.register(DirectorMediaImage)
class DirectorMediaImageAdmin(admin.ModelAdmin):
    list_display = ['director']
    search_fields = ['director']
    ordering = ['director']
