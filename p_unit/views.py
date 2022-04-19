from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import Unit_p
from .forms import UnitForm
from pengguna.decorators import allowed_user


# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def unitManage(request):
    units = Unit_p.objects.all()
    context = {
        'unit':units,
        'page_title':'Unit Manage',
    }
    return render(request, 'p_unit/unit_manage.html',context)


def unit_save_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            units = Unit_p.objects.all()
            data['html_unit_list'] = render_to_string('p_unit/unit_manage_list.html',{'unit':units})
        else:
            data['form_is_valid'] = False
    
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def createUnit(request):
    if request.method == 'POST':
        form = UnitForm(request.POST)
    else:
        form = UnitForm()
    return unit_save_form(request, form, 'p_unit/partunitcreate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def updateUnit(request,pk):
    unit = Unit_p.objects.get(id=pk)
    if request.method == 'POST':
        form = UnitForm(request.POST,instance=unit)
    else:
        form = UnitForm(instance=unit)
    
    return unit_save_form(request, form, 'p_unit/partunitupdate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def deleteUnit(request,pk):
    unit = Unit_p.objects.get(id=pk)
    data = dict()
    if request.method == 'POST':
        unit.delete()
        data['form_is_valid'] = True
        units = Unit_p.objects.all()
        data['html_unit_list'] = render_to_string('p_unit/unit_manage_list.html',{'unit':units},request=request)
    else:
        context = {
            'unit':unit,
        }
        data['html_form'] = render_to_string('p_unit/partunitdelete.html',context,request=request)
    
    return JsonResponse(data)

