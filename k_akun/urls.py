from django.urls import path, re_path

from .views import (
    manageAkun,
    createAkun,
    updateAkun,
    deleteAkun,
)
app_name = 'k_akun'
urlpatterns = [
    re_path(r'^delete-akun/(?P<pk>\d+)/$',deleteAkun,name='delete'),
    re_path(r'^edit-akun/(?P<pk>\d+)/$',updateAkun,name='edit'),
    path('create-akun/',createAkun,name='create'),
    path('',manageAkun,name='manage'),
]
