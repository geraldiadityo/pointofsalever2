from django.urls import path, re_path
from .views import (
    manageJurnalUmum,
    createJurnal,
    updateJurnal,
    deleteJurnal,
)

app_name='jurnal'

urlpatterns = [
    re_path(r'^delete-transaksi/(?P<pk>\d+)/$',deleteJurnal,name='delete'),
    re_path(r'^update-transaksi/(?P<pk>\d+)/$',updateJurnal,name='edit'),
    path('create-transaksi/',createJurnal,name='create'),
    path('',manageJurnalUmum,name='manage')
]