from django.urls import path, re_path
from .views import (
    homeView,
    get_by_akun,
)
app_name = 'bukubesar'
urlpatterns = [
    path('get-table',get_by_akun,name='get_table'),
    path('',homeView,name='home'),
]
