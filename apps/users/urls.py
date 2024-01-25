from django.urls import path

from apps.users.views import login_view, profile, change_avatar, logout_logics, change_profile, change_password, favorite_movie, signup_logics


urlpatterns = [
    path('login/', login_view, name="login"),
    path('profile/', profile, name="profile"),
    path('change_avatar/<int:pk>', change_avatar, name="change_avatar"),
    path('logout/', logout_logics, name="logout"),
    path('change_profile/<int:pk>', change_profile, name="change_profile"),
    path('password_change/<int:pk>', change_password, name="change_password"),
    path('favorite/', favorite_movie, name="favorite_movie"),
    path('sign_up/', signup_logics, name='sign_up')
]
