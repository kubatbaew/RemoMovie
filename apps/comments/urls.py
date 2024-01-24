from django.urls import path

from apps.comments.views import create_comment


urlpatterns = [
    path('create_comment/<int:pk>', create_comment, name="create_comment"),
]
