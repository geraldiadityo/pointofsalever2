from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Item_p
from .forms import ItemForm
from pengguna.decorators import allowed_user
# Create your views here.

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def itemManage(request):
    items = Item_p.objects.all().order_by('-created')
    context = {
        'page_title':'Item Manage',
        'item':items,
    }
    return render(request, 'p_item/item_manage.html',context)

def item_save_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = Item_p.objects.all().order_by('-created')
            data['html_item_list'] = render_to_string('p_item/item_manage_list.html',{'item':items})
        else:
            data['form_is_valid'] = False
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return  JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def createItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
    else:
        form = ItemForm()
    return item_save_form(request, form, 'p_item/partcreateitem.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def updateItem(request,pk):
    item = Item_p.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
    else:
        form = ItemForm(instance=item)
    
    return item_save_form(request, form, 'p_item/partitemupdate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def deleteItem(request,pk):
    data = dict()
    item = Item_p.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        data['form_is_valid'] = True
        items = Item_p.objects.all().order_by('-created')
        data['html_item_list'] = render_to_string('p_item/item_manage_list.html',{'item':items},request=request)
    else:
        context = {
            'item':item,
        }
        data['html_form'] = render_to_string('p_item/partitemdelete.html',context,request=request)
    return JsonResponse(data)


@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','kasir'])
def viewDetail(request,pk):
    item = Item_p.objects.get(id=pk)
    data = dict()
    context = {
        'item':item,
    }
    data['html_form'] = render_to_string('p_item/view_item_detail.html',context,request=request)
    return JsonResponse(data)
