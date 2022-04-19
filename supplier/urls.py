from django.urls import path,re_path

from .views import (
    supplierManage,
    createSupplier,
    updateSupplier,
    deleteSupplier
)
app_name = 'supplier'
urlpatterns = [
    re_path(r'^delete-supplier/(?P<pk>\d+)/$',deleteSupplier,name='delete'),
    re_path(r'^update-supplier/(?P<pk>\d+)/$',updateSupplier,name='update'),
    path('create-supplier/',createSupplier,name='create'),
    path('',supplierManage,name='manage'),
]
