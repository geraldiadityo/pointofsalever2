from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Supplier
from .forms import SupplierForm

from pengguna.decorators import allowed_user

# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def supplierManage(request):
    supplier = Supplier.objects.all().order_by('-created')
    context = {
        'supplier':supplier,
        'page_title':'Supplier Manage',
    }
    return render(request, 'supplier/supplier_manage.html',context)

def supplier_save_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            suppliers = Supplier.objects.all().order_by('-created')
            data['html_supplier_list'] = render_to_string('supplier/supplier_manage_list.html',{'supplier':suppliers})
        else:
            data['form_is_valid'] = False
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context, request=request)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def createSupplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
    else:
        form = SupplierForm()
    
    return supplier_save_form(request, form, 'supplier/partsuppliercreate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def updateSupplier(request,pk):
    supplier = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST,instance=supplier)
    else:
        form = SupplierForm(instance=supplier)
    
    return supplier_save_form(request, form, 'supplier/partsupplierupdate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def deleteSupplier(request,pk):
    supplier = Supplier.objects.get(id=pk)
    data = dict()
    if request.method == 'POST':
        supplier.delete()
        data['form_is_valid'] = True
        suppliers = Supplier.objects.all().order_by('-created')
        data['html_supplier_list'] = render_to_string('supplier/supplier_manage_list.html',{'supplier':suppliers},request=request)
    else:
        context = {
            'supplier':supplier,
        }
        data['html_form'] = render_to_string('supplier/partsupplierdelete.html',context,request=request)
    return JsonResponse(data)

