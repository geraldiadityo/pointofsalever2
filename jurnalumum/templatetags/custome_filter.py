from django import template
from jurnalumum.models import Jurnal

register = template.Library()

@register.inclusion_tag('jurnal/data_jurnal.html')
def loadByTgl(tgl):
    datalist = Jurnal.objects.filter(tgl=tgl)
    return {"databytgl":datalist}

