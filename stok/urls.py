from django.urls import path,re_path

from .views import *

app_name='stok'
urlpatterns = [
    re_path(r'^stok-manage/(?P<tipe>[\w]+)/$',manageStok,name='manage'),
    re_path(r'^detail-stokin/(?P<pk>\d+)/$',detail_stokin,name='detail-stokin'),
    re_path(r'^delete-stok/(?P<pk>\d+)/$',deleteStok,name='delete-stok'),
    path('create-stok-out/',createStokOut,name='stokout_create'),
    path('create-stok-in/',createStokIn,name='stokin_create'),
    path('selected-product-stokin/',selectedProductStokin,name='selected-product-stokin'),
    path('get_total/',getTotal,name='get_total'),
    path('data-item/',dataItemforStok,name='data-item-search'),
]