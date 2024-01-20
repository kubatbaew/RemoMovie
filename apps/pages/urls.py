from django.urls import path

from apps.pages.views import homepage


urlpatterns = [
    path('', homepage, name="homepage"),
]