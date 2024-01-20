from django.contrib import admin

from apps.genres.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
