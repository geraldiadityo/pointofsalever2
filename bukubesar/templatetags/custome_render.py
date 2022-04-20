from django import template
from jurnalumum.models import Jurnal
register = template.Library()
@register.inclusion_tag('bukubesar/data_jurnal.html')
def loadDataAkunTgl(tgl = None,akun=None):
    if tgl == None or akun == None:
        datalist = {}
    else:
        datalist = Jurnal.objects.filter(akun_id=akun).filter(tgl=tgl)
    
    return {'datalist':datalist}

