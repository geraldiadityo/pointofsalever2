from django.urls import path,re_path

from .views import (
    itemManage,
    createItem,
    updateItem,
    deleteItem,
    viewDetail,
)
app_name='p_item'
urlpatterns = [
    re_path(r'^detail-item/(?P<pk>\d+)/$',viewDetail,name='view_detail'),
    re_path(r'^delete-item/(?P<pk>\d+)/$',deleteItem,name='delete'),
    re_path(r'^update-item/(?P<pk>\d+)/$',updateItem,name='update'),
    path('create-item/',createItem,name='create'),
    path('',itemManage,name='manage'),
]