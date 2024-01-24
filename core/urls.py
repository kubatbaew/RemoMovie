from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.pages.urls')),
    path('', include('apps.movies.urls')),
    path('', include('apps.celebrities.urls')),
    path('', include('apps.news.urls')),
    path('', include('apps.comments.urls')),
    path('', include('apps.users.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.IMAGES_URL, document_root=settings.IMAGES_ROOT)
