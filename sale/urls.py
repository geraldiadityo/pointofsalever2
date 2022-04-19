from django.urls import path,re_path

from .views import *

app_name = 'sale'
urlpatterns = [
    path('delete-keranjang/',deleteItemKeranjang,name='keranjang-delete'),
    path('add-cart/',addKeranjang,name='add-cart'),
    path('kembalian/',kembalian,name='kembalian'),
    path('search-barcode/',searchBarcode,name='search-barcode'),
    path('data-item/',dataItemforSale,name='dataitem'),
    path('sale-view/',saleView,name='sale_view'),
    path('cetak-faktur/',cetakFaktur,name='cetak_faktur'),
    path('delete-all-item-keranjang/',deleteAllInKeranjang,name='delete-all-cart'),
    path('data-item/',dataItemforSale,name='data-item'),
]
