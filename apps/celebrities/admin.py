from django.contrib import admin

from apps.celebrities.models import Celebrity, Director


@admin.register(Celebrity)
class CelebrityAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    search_fields = ['full_name']
    ordering = ['full_name', 'prof', 'country']


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    search_fields = ['full_name']
    ordering = ['full_name', 'country']
