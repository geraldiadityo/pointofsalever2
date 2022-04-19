from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

# Create your views here.
from datetime import datetime
from .models import StokM
from .forms import StokInForm,StokOutForm
from p_item.models import Item_p
from pengguna.decorators import (
    allowed_user,
)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def manageStok(request,tipe):
    datastok = StokM.objects.filter(tipe=tipe)
    if tipe == 'out' or tipe == 'OUT' or tipe == 'Out':
        data_template = 'stok/stokout_manage.html'
    elif tipe == 'in' or tipe == 'IN' or tipe == 'In':
        datenow = datetime.now().date()
        dataexpired = datastok.filter(tipe='in')
        if dataexpired.filter(expired_date=datenow).exists():
            data_expired = dataexpired.filter(expired_date=datenow)
            for i in data_expired:
                stokout = StokM.objects.create(tipe='out',product_id=i.product_id,detail='expired',qty=i.qty,hargabeli=i.hargabeli,total=i.total,expired_date=i.expired_date)
                stokout.save()
                stokin = StokM.objects.get(id=i.id)
                stokin.expired_date = None
                stokin.save()
                item = Item_p.objects.get(pk=i.product_id)
                stokupdate = int(item.stok) - int(i.qty)
                item.stok = stokupdate
                item.save()
        data_template = 'stok/stokin_manage.html'
    
    context = {
        'page_title':'Manage Stok'+tipe,
        'datastok':datastok.order_by('-tanggal'),
    }
    return render(request, data_template,context)

def dataItemforStok(request):
    dataitem = Item_p.objects.all()
    data = dict()
    context = {
        'item':dataitem,
    }
    data['html_form'] = render_to_string('stok/data_item.html',context,request=request)
    return JsonResponse(data)

def selectedProductStokin(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        itemid = request.GET.get('field_value')
        dataitem = Item_p.objects.get(pk=itemid)
        data['itemid'] = itemid
        data['unit'] = dataitem.unit.nama
        data['stok_awal'] = dataitem.stok
        return JsonResponse(data)
    return JsonResponse({},status=400)

def getTotal(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        hargabeli = request.GET.get('hargabeli')
        qty = request.GET.get('qty')
        total = int(qty) * int(hargabeli)
        data['totalharga'] = total
        return JsonResponse(data)
    return JsonResponse({},status=400)


@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def createStokIn(request):
    form = StokInForm(initial={'tipe':'in'})
    if request.method == 'POST':
        form = StokInForm(request.POST, initial={'tipe':'in'})
        if form.is_valid():
            form.save()
            qty = form.cleaned_data.get('qty')
            hargabeli = form.cleaned_data.get('hargabeli')
            hargajual = (int(hargabeli) * (10/100)) + int(hargabeli)
            item = request.POST['item_id']
            stok_awal = request.POST['stok_awal']
            isistok = int(stok_awal) + int(qty)
            dataitem = Item_p.objects.get(pk=item)
            dataitem.stok = isistok
            dataitem.hargaawal = int(hargabeli)
            dataitem.harga = hargajual
            dataitem.save()
            tipe = {
                'tipe':form.cleaned_data.get('tipe')
            }
            return HttpResponse(
                '<script>alert("data action success");window.location="'+str(reverse_lazy('stok:manage',kwargs=tipe))+'";</script>'
            )
    
    context = {
        'page_title':'Stok In Add',
        'form':form,
    }
    return render(request, 'stok/create_stokin.html',context)

def detail_stokin(request,pk):
    data = dict()
    datastok = StokM.objects.get(id=pk)
    tipe = datastok.tipe
    if tipe == 'in' or tipe == 'IN':
        datatemplate = 'stok/stokin-detail.html'
    else:
        datatemplate = 'stok/stokout-detail.html'
    context = {
        'stok_item':datastok,
        'tipe':tipe,
    }
    data['html_form'] = render_to_string(datatemplate,context,request=request)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def deleteStok(request,pk):
    data = dict()
    stok = StokM.objects.get(id=pk)
    tipe = stok.tipe
    if tipe == 'in' or tipe == 'IN' or tipe == 'In':
        datatemplate = 'stok/stokin_manage_list.html'
    else:
        datatemplate = 'stok/stokout_manage_list.html'

    if request.method == 'POST':
        stok.delete()
        data['form_is_valid'] = True
        datastok = StokM.objects.filter(tipe=tipe).order_by('-tanggal')
        data['html_stok_list'] = render_to_string(datatemplate,{'datastok':datastok},request=request)
    else:
        context = {
            'stok':stok,
            'tipe':tipe,
        }
        data['html_form'] = render_to_string('stok/stokin-delete.html',context,request=request)
    
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def createStokOut(request):
    form = StokOutForm(initial={'tipe':'out'})
    if request.method == 'POST':
        form = StokOutForm(request.POST, initial={'tipe':'out'})
        if form.is_valid():
            form.save()
            qty = form.cleaned_data.get('qty')
            item = request.POST['item_id']
            stok_awal = request.POST['stok_awal']
            isistok = int(stok_awal) - int(qty)
            dataitem = Item_p.objects.get(pk=item)
            dataitem.stok = isistok
            dataitem.save()
            tipe = {
                'tipe':form.cleaned_data.get('tipe'),
            }
            return HttpResponse(
                '<script>alert("data action success");window.location="'+str(reverse_lazy('stok:manage',kwargs=tipe))+'";</script>'
            )
    context = {
        'page_title':'Stok out Add',
        'form':form,
    }
    return render(request, 'stok/create_stokout.html',context)
