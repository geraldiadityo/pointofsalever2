from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from p_item.models import Item_p
from supplier.models import Supplier
from sale.models import SaleModel
from datetime import datetime

@login_required(login_url='pengguna:login')
def index(request):
    count_item = Item_p.objects.all().count()
    count_supplier = Supplier.objects.all().count()
    count_sale = SaleModel.objects.filter(tanggal=datetime.now().date()).count()
    context = {
        'supplierCount':count_supplier,
        'saleCount':count_sale,
        'itemCount':count_item,
        'page_title':'Dashboard',
        'role':request.user.groups.all()[0].name,
    }
    return render(request, 'dashboard.html',context)

