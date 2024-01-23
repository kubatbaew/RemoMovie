from django.contrib import admin

from apps.trailers.models import Trailer


@admin.register(Trailer)
class TrailerAdmin(admin.ModelAdmin):
    list_display = ['movie']
    search_fields = ['movie']
