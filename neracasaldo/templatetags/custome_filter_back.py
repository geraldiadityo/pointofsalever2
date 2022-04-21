from django import template
from jurnalumum.models import Jurnal
register = template.Library()

@register.inclusion_tag('neracasaldo/data_jurnal.html')
def getTotalSaldo(akun):
    datalist = Jurnal.objects.filter(akun_id=akun)
    Debet_saldo = 0
    Kredit_saldo = 0
    for i in datalist:
        if i.tipe == 'Debet':
            Debet_saldo += i.nominal
        else:
            Kredit_saldo += i.nominal
    
    total_saldo = abs(Debet_saldo - Kredit_saldo)
    return {'totalsaldo':total_saldo}