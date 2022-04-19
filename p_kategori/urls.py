from django.urls import path,re_path

from .views import (
    kategoriManage,
    createKategori,
    updateKategori,
    deleteKategori,
)

app_name = 'p_kategori'
urlpatterns = [
    re_path(r'^delete-kategori/(?P<pk>\d+)/$',deleteKategori,name='delete'),
    re_path(r'^update-kategori/(?P<pk>\d+)/$',updateKategori,name='update'),
    path('create-kategori/',createKategori,name='create'),
    path('',kategoriManage,name='manage'),
]