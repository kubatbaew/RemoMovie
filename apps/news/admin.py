from django.contrib import admin

from apps.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
