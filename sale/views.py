from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse
from django.urls import reverse_lazy
import datetime
from django.contrib.auth.decorators import login_required

from .models import (
    SaleModel,
    KeranjangModel,
)
from p_item.models import Item_p
from .forms import (
    SaleForm,
    KeranjangForm,
)

from jurnalumum.models import Jurnal

from pengguna.decorators import allowed_user
# Create your views here.

def toRupiah(data):
    y = str(data)
    if len(y) <=3:
        return "Rp {}".format(y)
    else:
        p = y[-3:]
        q = y[:-3]
        return toRupiah(q) +'.'+p
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def saleView(request):
    lastsale = SaleModel.objects.all().order_by('id').last()
    thisday = str(datetime.datetime.now().date())
    split_day = thisday.split('-')
    middleinvoice = split_day[0] + split_day[1] + split_day[2]
    if not lastsale:
        numberinvoice = "GE"+middleinvoice+"0001"
    else:
        if str(lastsale.tanggal) != thisday:
            numberinvoice = "GE"+middleinvoice+"0001"
        else:
            lastinvoice = str(lastsale.invoice)
            int_number = int(lastinvoice.split("GE")[-1])
            new_number = int_number + 1
            numberinvoice = "GE"+str(new_number)
    
    datakeranjang = KeranjangModel.objects.all()
    if request.method == 'POST':
        form_sale = SaleForm(request.POST,initial={'invoice':numberinvoice})
        if form_sale.is_valid():
            pendapatan = int(form_sale.cleaned_data.get('total_pendapatan'))
            form_sale.save()
            for i in datakeranjang:
                itemkeranjang = KeranjangModel.objects.get(id=i.id)
                stok = Item_p.objects.get(id=itemkeranjang.product.id)
                stokawal = stok.stok
                stok.stok = stokawal - i.qty
                stok.save()
            tgl_now = datetime.datetime.now().date()
            datajurnal = Jurnal.objects.filter(tgl=tgl_now).filter(ket='Pendapatan Penjualan')
            if datajurnal.exists():
                for x in datajurnal:
                    new_update_jurnal = datajurnal.get(akun=x.akun)
                    new_update_jurnal.nominal = int(new_update_jurnal.nominal) + pendapatan
                    new_update_jurnal.save()
            else:
                new_jurnal = Jurnal.objects.create(tgl=tgl_now,akun_id='1',ket='Pendapatan Penjualan',ref='',nominal=pendapatan,tipe='Debet')
                new_jurnal.save()
                new_jurnal = Jurnal.objects.create(tgl=tgl_now,akun_id='4',ket='Pendapatan Penjualan',ref='',nominal=pendapatan,tipe='Kredit')
                new_jurnal.save()
            return HttpResponse(
                '<script>confirm("Cetak Faktur ?") ? window.location="'+str(reverse_lazy('sale:cetak_faktur'))+'" : window.location="'+str(reverse_lazy('sale:delete-all-cart'))+'" </script>'
            )
    form_sale = SaleForm(initial={'invoice':numberinvoice})
    context = {
        'form':form_sale,
        'page_title':'Sale Form',
        'keranjang':datakeranjang,
        'invoice':numberinvoice,
    }
    return render(request, 'sale/sale.html',context)

def deleteAllInKeranjang(request):
    itemkeranjang = KeranjangModel.objects.all()
    itemkeranjang.delete()
    return HttpResponse(
        '<script>alert("transaction success");window.location="'+str(reverse_lazy('sale:sale_view'))+'";</script>'
    )
    

def cetakFaktur(request):
    itemkeranjang = KeranjangModel.objects.all()
    total = 0
    total_disc = 0
    for i in itemkeranjang:
        total += i.totalharga
        total_disc += i.discount
    
    total_seluruh = total - total_disc
    context = {
        'datakeranjang':itemkeranjang,
        'total':total,
        'total_disc':total_disc,
        'totalall':total_seluruh,
    }
    return render(request, 'sale/cetak_faktur.html',context)


def dataItemforSale(request):
    data = dict()
    dataitem = Item_p.objects.all()
    context = {
        'item':dataitem,
    }
    data['html_form'] = render_to_string('sale/dataitem.html',{'item':dataitem},request=request)
    return JsonResponse(data)

def searchBarcode(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        barcode = request.GET.get('barcode')
        dataitem = Item_p.objects.get(barcode=barcode)
        data['product_id'] = dataitem.pk
        data['harga'] = dataitem.harga
        return JsonResponse(data)
    return JsonResponse({},status=400)

def addKeranjang(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        itemid = request.GET.get('itemid')
        dataitem = Item_p.objects.get(id=itemid)
        harga = request.GET.get('harga')
        qty = request.GET.get('qty')
        hargaawal = dataitem.hargaawal
        discount = 0
        totalhargaawal = hargaawal * int(qty)
        totalharga = int(harga) * int(qty)
        totaluntung = totalharga - totalhargaawal
        keranjang = KeranjangModel.objects.create(totalharga=totalharga,discount=discount,product=dataitem,qty=qty,total_untung=totaluntung)
        keranjang.save()
        datakeranjang = KeranjangModel.objects.all()
        totalbyr = 0
        ttluntung = 0
        
        for i in datakeranjang:
            totalbyr += i.totalharga
            ttluntung += i.total_untung
        
        data['totalbyr'] = totalbyr
        data['discount'] = discount
        data['totaluntung'] = ttluntung
        data['grand_total'] = toRupiah(totalbyr)
        data['html_keranjang_list'] = render_to_string('sale/keranjang.html',{'keranjang':datakeranjang},request=request)
        return JsonResponse(data)
    return JsonResponse({},status=400)

def kembalian(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        cash = request.GET.get('cash')
        totalbyr = request.GET.get('totalbyr')
        ttl_kembalian = int(cash) - int(totalbyr)
        data['kembalian'] = ttl_kembalian
        return JsonResponse(data)
    return JsonResponse({},status=400)

def deleteItemKeranjang(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        keranjangid = request.GET.get('keranjangid')
        keranjangitem = KeranjangModel.objects.get(id=keranjangid)
        keranjangitem.delete()
        totalbyr = 0
        totalpendapatan = 0
        datakeranjang = KeranjangModel.objects.all()
        
        for i in datakeranjang:
            totalbyr += i.totalharga
            totalpendapatan += i.total_untung
        
        data['totalbyr'] = totalbyr
        data['total_untung'] = totalpendapatan
        data['grand_total'] = toRupiah(totalbyr)
        data['html_keranjang_list'] = render_to_string('sale/keranjang.html',{'keranjang':datakeranjang},request=request)
        return JsonResponse(data)
    return JsonResponse({},status=400)

