from django.urls import path,re_path
from .views import viewNeracaSaldo

app_name = 'neracasaldo'
urlpatterns = [
    path('',viewNeracaSaldo,name='view'),
]

