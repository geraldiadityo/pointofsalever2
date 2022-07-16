from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
from django.template.loader import render_to_string
from .utils import render_to_pdf
from django.contrib.auth.decorators import login_required

from sale.models import SaleModel
from stok.models import StokM
from p_item.models import Item_p
import re

from pengguna.decorators import allowed_user

# Create your views here.

def cekTanggalregex(data):
    x = re.search(r"[0-9]{4}[\w-][0-9]{2}[\w-][0-9]{2}", str(data))
    if x  == None:
        return False
    else:
        return True


def cekBulanregex(data):
    x = re.search(r"[0-9]{4}[\w-][0-9]{2}", str(data))
    if x == None:
        return False
    else:
        return True
    


def viewPDFpenjualan(request,tanggal):
    if tanggal == '0' or tanggal == 0:
        datasale = SaleModel.objects.all().order_by('-tanggal')
    else:
        if cekTanggalregex(tanggal) == True:
            datasale = SaleModel.objects.filter(tanggal=tanggal).order_by('-tanggal')
        elif cekBulanregex(tanggal) == True:
            val_bulan = tanggal.split('-')
            datatahun = val_bulan[0]
            databulan = val_bulan[1]
            datasale = SaleModel.objects.filter(tanggal__year=datatahun).filter(tanggal__month=databulan).order_by('-tanggal')
        else:
            datasale = SaleModel.objects.filter(tanggal__year=tanggal).order_by('-tanggal')
    
    total = 0
    keuntungan = 0
    for i in datasale:
        total += i.total_bayar
        keuntungan += i.total_pendapatan
    
    context = {
        'page_title':'Laporan Keuangan',
        'sale':datasale,
        'tanggal':tanggal,
        'total':total,
        'keuntungan':keuntungan,
    }

    pdf = render_to_pdf('laporan/reporting_penjualan.html', context)
    return HttpResponse(pdf,content_type="application/pdf")


def downloadPDFpenjualan(request,tanggal):
    if tanggal == '0' or tanggal == 0 or tanggal == None:
        datasale = SaleModel.objects.all().order_by('-tanggal')
    else:
        if cekTanggalregex(tanggal) == True:
            datasale = SaleModel.objects.filter(tanggal=tanggal).order_by('-tanggal')
        elif cekBulanregex(tanggal) == True:
            val_bulan = tanggal.split('-')
            datatahun = val_bulan[0]
            databulan = val_bulan[1]
            datasale = SaleModel.objects.filter(tanggal__year=datatahun).filter(tanggal__month=databulan).order_by('-tanggal')
        else:
            datasale = SaleModel.objects.filter(tanggal__year=tanggal).order_by('-tanggal')
    
    context = {
        'sale':datasale,
        'tanggal':tanggal,
    }
    pdf = render_to_pdf('laporan/laporan_penjualan.html', context)
    response = HttpResponse(pdf,content_type="applicaation/pdf")
    filename = "laporan_penjualan.pdf"
    content = "attachment; filename=%s" %(filename)
    response['Content-Dispotition'] = content
    return response

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def laporanSale(request):
    datasale = SaleModel.objects.all().order_by('-tanggal')
    datatanggal = SaleModel.objects.values_list('tanggal',flat=True).distinct()
    databulan = SaleModel.objects.dates('tanggal', 'month',order='DESC')
    datatahun = SaleModel.objects.dates('tanggal', 'year',order='DESC')
    context = {
        'page_title':'Data Penjualan',
        'sale':datasale,
        'tanggal':datatanggal,
        'bulan':databulan,
        'tahun':datatahun,
    }
    return render(request, 'laporan/penjualan.html',context)

@allowed_user(allowed_roles=['admin'])
def laporanSaleDate(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        value = str(request.GET.get('value'))
        if value == '0' or value == 0 or value == None:
            datasale = SaleModel.objects.all().order_by('-tanggal')
        else:
            if cekTanggalregex(value) == True:
                datasale = SaleModel.objects.filter(tanggal=value).order_by('-tanggal')
            elif cekBulanregex(value) == True:
                val_bulan = value.split('-')
                datatahun = val_bulan[0]
                databulan = val_bulan[1]
                datasale = SaleModel.objects.filter(tanggal__year=datatahun).filter(tanggal__month=databulan).filter('-tanggal')
            else:
                datasale = SaleModel.objects.filter(tanggal__year=value).order_by('-tanggal')
        data['html_sale_list'] = render_to_string('laporan/table_penjualan.html',{'sale':datasale},request=request)
        return JsonResponse(data)
    return JsonResponse({},status=400)


@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def stoklaporan(request,tipe):
    if tipe == 'in' or tipe == 'In' or tipe == 'IN':
        data_template = 'laporan/laporan_stok_in.html'
    elif tipe == 'out' or tipe == 'Out' or tipe == 'OUT':
        data_template = 'laporan/laporan_stok_out.html'
    
    datastok = StokM.objects.filter(tipe=tipe).order_by('-tanggal')
    datatanggal = datastok.dates('tanggal', 'day',order='DESC')
    databulan = datastok.dates('tanggal', 'month',order='DESC')
    datatahun = datastok.dates('tanggal', 'year',order='DESC')

    context = {
        'page_title':'Stok {}'.format(tipe),
        'stok':datastok,
        'tanggal':datatanggal,
        'bulan':databulan,
        'tahun':datatahun,
        'tipe':tipe,
    }
    return render(request, data_template,context)

def stokLaporanDates(request,tipe):
    data = dict()
    if tipe == 'in' or tipe == 'IN' or tipe == 'In':
        data_template = 'laporan/table_stok_in.html'
    elif tipe == 'out' or tipe == 'OUT' or tipe == 'Out':
        data_template = 'laporan/table_stok_out.html'
    
    if request.is_ajax and request.method == 'GET':
        value = str(request.GET.get('value'))
        dataset = StokM.objects.filter(tipe=tipe)
        if value == '0' or value == None:
            datastok = dataset.order_by('-tanggal')
        else:
            if cekTanggalregex(value) == True:
                datastok = dataset.filter(tanggal__date=value).order_by('-tanggal')
            elif cekBulanregex(value) == True:
                val_bulan = value.split('-')
                datatahun = val_bulan[0]
                databulan = val_bulan[1]
                datastok = dataset.filter(tanggal__year=datatahun).filter(tanggal__month=databulan).order_by('-tanggal')
            else:
                datastok = dataset.filter(tanggal__year=value)
        data['html_stok_list'] = render_to_string(data_template,{'stok':datastok},request=request)
        return JsonResponse(data)
    return JsonResponse({},status=400)

def stokViewPdf(request,tipe,tanggal):
    if tipe == 'in' or tipe == 'IN':
        datatemplate = 'laporan/reporting_stok_in.html'
    elif tipe == 'out' or tipe == 'OUT':
        datatemplate = 'laporan/reporting_stok_out.html'
    
    dataset = StokM.objects.filter(tipe=tipe)
    if tanggal == '0' or tanggal == 0 or tanggal == None:
        datastok = dataset.order_by('-tanggal')
    else:
        if cekTanggalregex(tanggal) == True:
            datastok = dataset.filter(tanggal__date=tanggal).order_by('-tanggal')
        elif cekBulanregex(tanggal) == True:
            val_bulan = tanggal.split('-')
            datatahun = val_bulan[0]
            databulan = val_bulan[1]
            datastok = dataset.filter(tanggal__year=datatahun).filter(tanggal__month=databulan).order_by('-tanggal')
        else:
            datastok = dataset.filter(tanggal__year=tanggal).order_by('-tanggal')
    
    total = 0
    for i in datastok:
        total += i.total
    
    context = {
        'stok':datastok,
        'tanggal':tanggal,
        'total':total,
    }
    pdf = render_to_pdf(datatemplate, context)
    return HttpResponse(pdf,content_type="application/pdf")


def stokDownloadPDF(request,tipe,tanggal):
    if tipe == 'in' or tipe == 'IN' or tipe == 'In':
        datatemplate = 'laporan/reporting_stok_in.html'
    elif tipe == 'out' or tipe == 'OUT':
        datatemplate == 'laporan/reporting_stok_out.html'
    
    dataset = StokM.objects.filter(tipe=tipe)
    if tanggal == '0' or tanggal == 0 or tanggal == None:
        datastok = dataset.order_by('-tanggal')
    else:
        if cekTanggalregex(tanggal) == True:
            datastok = dataset.filter(tanggal=tanggal).order_by('-tanggal')
        elif cekBulanregex(tanggal) == True:
            val_bulan = tanggal.split('-')
            datatahun = val_bulan[0]
            databulan = val_bulan[1]
            datastok = dataset.filter(tanggal__year=datatahun).filter(tanggal__month=databulan).order_by('-tanggal')
        else:
            datastok = dataset.filter(tanggal__year=tanggal).order_by('-tanggal')
    
    total = 0
    for i in datastok:
        total += i.total
    
    context = {
        'stok':datastok,
        'tanggal':tanggal,
        'total':total,
    }
    pdf = render_to_pdf(datatemplate, context)
    response = HttpResponse(pdf,content_type="application/pdf")
    filename = "laporan Stok {}".format(tipe)
    content = "attachment; filename=%s" %(filename)
    response['Content-Disposition'] = content
    return response

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def stokOpname(request):
    dataitem = Item_p.objects.all().order_by('-created')
    context = {
        'page_title':'Stok Opname',
        'item':dataitem,
    }
    return render(request, 'laporan/laporan_stok_opname',context)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def ringkasanLaporan(request):
    pembelian = StokM.objects.filter(tipe='in')
    penjualan = SaleModel.objects.all()
    context = {
        'data_pembelian':pembelian,
        'data_penjualan':penjualan,
        'page_title':'Ringkasan Laporan',
    }
    return render(request)
