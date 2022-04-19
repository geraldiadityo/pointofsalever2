from django.urls import path,re_path

from .views import (
    unitManage,
    createUnit,
    updateUnit,
    deleteUnit,
)

app_name = 'p_unit'

urlpatterns = [
    re_path(r'^delete-unit/(?P<pk>\d+)/$',deleteUnit,name='delete'),
    re_path(r'^update-unit/(?P<pk>\d+)/$',updateUnit,name='update'),
    path('create-unit/',createUnit,name='create'),
    path('',unitManage,name='manage'),
]