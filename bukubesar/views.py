from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from k_akun.models import Akun
from jurnalumum.models import Jurnal

from pengguna.decorators import (
    allowed_user,
)

# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def homeView(request):
    akun_list = Akun.objects.all()
    context = {
        'akun_list':akun_list,
        'page_title':'Postingan Buku Besar',
    }
    return render(request, 'bukubesar/home_bukubesar.html',context)

def get_by_akun(request):
    data = dict()
    if request.is_ajax and request.method == 'GET':
        akun_id = request.GET.get('akun_id')
        nama = request.GET.get('nama')
        cek_kategori_akun = Akun.objects.get(id=akun_id)
        data_transaksi = Jurnal.objects.filter(akun_id=akun_id).order_by('tgl')
        tgl_list = data_transaksi.values_list('tgl',flat=True).order_by('tgl').distinct()
        total_debet = 0
        total_kredit = 0
        for i in data_transaksi:
            if i.tipe == 'Debet':
                total_debet += i.nominal
            else:
                total_kredit += i.nominal
        
        total_saldo = total_debet - total_kredit
        
        context_data = {
            'tgl_list':tgl_list,
            'akun':akun_id,
            'total_debet':total_debet,
            'total_kredit':total_kredit,
            'total_saldo':abs(total_saldo),
        }
        data['kategori_akun'] = cek_kategori_akun.kategori
        data['nama_akun'] = nama
        data['html_bukubesar_list'] = render_to_string('bukubesar/data_table.html',context_data,request=request)
        return JsonResponse(data)
    return JsonResponse({},status=400)
