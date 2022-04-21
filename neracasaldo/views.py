from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from k_akun.models import Akun
from jurnalumum.models import Jurnal

from pengguna.decorators import (
    allowed_user,
)
# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def viewNeracaSaldo(request):
    akun_list = Akun.objects.all()

    total_saldo_debet = 0
    total_saldo_kredit = 0
    for i in akun_list:
        data_jurnal = Jurnal.objects.filter(akun_id=i.id)
        saldo_debet = 0
        saldo_kredit = 0
        for x in data_jurnal:
            if x.tipe == 'Debet':
                saldo_debet += x.nominal
            else:
                saldo_kredit += x.nominal
            
        total_saldo = abs(saldo_debet - saldo_kredit)
        if i.kategori == 'Debet':
            total_saldo_debet += total_saldo
        else:
            total_saldo_kredit += total_saldo
    
    context = {
        'akunlist':akun_list,
        'total_saldo_debet':total_saldo_debet,
        'total_saldo_kredit':total_saldo_kredit,
        'page_title':'Neraca Saldo',
    }
    return render(request, 'neracasaldo/view_neraca_saldo.html',context)

