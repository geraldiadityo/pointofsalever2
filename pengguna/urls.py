from django.urls import path,re_path

from .views import *

app_name = 'pengguna'

urlpatterns = [
    path('login-pengguna/',loginView,name='login'),
    path('logout-pengguna/',logoutView,name='logout'),
    path('create-pengguna/',register,name='create_pengguna'),
    path('profile-setting/',editProfilePengguna,name='profile_setting'),
    re_path(r'^delete-pengguna/(?P<pk>\d+)/$',deletePengguna,name='delete'),
    re_path(r'^view-pengguna/(?P<pk>\d+)/$',viewPengguna,name='view_pengguna'),
    path('',managePengguna,name='manage'),
]