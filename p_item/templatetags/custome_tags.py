from django import template
import locale

register = template.Library()

def to_rupiah(data):
    y = str(data)
    if len(y) <= 3:
        return "Rp {}".format(y)
    else:
        p = y[-3:]
        q = y[:-3]
        return to_rupiah(q) + '.' + p

register.filter('to_rupiah',to_rupiah)
