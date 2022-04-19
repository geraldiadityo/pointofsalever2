from django.urls import path,re_path

from .views import (
    laporanSale,
    laporanSaleDate,
    stoklaporan,
    stokLaporanDates,
    stokViewPdf,
    stokDownloadPDF,
    viewPDFpenjualan,
    downloadPDFpenjualan,
)

app_name = 'laporan'

urlpatterns = [
    re_path(r'^stok-download-reporting-date/(?P<tipe>[\w]+)/(?P<tanggal>[\w-]+)/$',stokDownloadPDF,name='stok_download_pdf'),
    re_path(r'^stok-view-reporting-date/([\w]+)/([\w-]+)/$',stokViewPdf,name='stok_view_pdf'),
    re_path(r'^stok-reporting/(?P<tipe>[\w]+)/$',stoklaporan,name='stok-reporting'),
    re_path(r'^stok-reporting-date/([\w]+)/$',stokLaporanDates,name='stok-reporting-date'),
    re_path(r'^sale-download-reporting-date/([\w-]+)/$',downloadPDFpenjualan,name='sale_download_pdf'),
    re_path(r'^sale-view-reporting-date/([\w-]+)/$',viewPDFpenjualan,name='sale_view_pdf'),
    path('sale-reporting/',laporanSale,name='penjualan-reporting'),
    path('sale-reporting-date/',laporanSaleDate,name='penjualan-tanggal'),
]