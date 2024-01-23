from django.urls import path

from apps.celebrities.views import CelebrityListView, CelebrityDetailView, DirectorDetailView


urlpatterns = [
    path('celebrities/', CelebrityListView.as_view(), name="celebrities"),
    path('celebrities/<int:pk>', CelebrityDetailView.as_view(), name="celebrity_detail"),

    path('director/<int:pk>', DirectorDetailView.as_view(), name="director_detail"),
]
