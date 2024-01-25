from django.urls import path

from apps.users.views import login_view, UserDetailView, change_avatar


urlpatterns = [
    path('login/', login_view, name="login"),
    path('profile/<int:pk>', UserDetailView.as_view(), name="profile"),
    path('change_avatar/<int:pk>', change_avatar, name="change_avatar"),
]
