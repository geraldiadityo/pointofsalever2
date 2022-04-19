from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Akun
from .forms import AkunForm

from pengguna.decorators import (
    allowed_user
)
# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(['kasir','admin'])
def manageAkun(request):
    akunlist = Akun.objects.all()
    context = {
        'page_title':'Akun Keuangan',
        'akunlist':akunlist,
    }
    return render(request, 'k_akun/akun_manage.html',context)

def akun_save_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            akunlist = Akun.objects.all()
            data['html_akun_list'] = render_to_string('k_akun/akun_manage_list.html',{'akunlist':akunlist})
        else:
            data['form_is_valid'] = False
    
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def createAkun(request):
    if request.method == 'POST':
        form = AkunForm(request.POST)
    else:
        form = AkunForm()
    
    return akun_save_form(request, form, 'k_akun/partakuncreate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def updateAkun(request, pk):
    akun = Akun.objects.get(id=pk)
    if request.method == 'POST':
        form = AkunForm(request.POST, instance=akun)
    else:
        form = AkunForm(instance=akun)
    
    return akun_save_form(request, form, 'k_akun/partakunupdate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def deleteAkun(request,pk):
    data = dict()
    akun = Akun.objects.get(id=pk)
    if request.method == 'POST':
        akun.delete()
        data['form_is_valid'] = True
        akunlist = Akun.objects.all()
        data['html_akun_list'] = render_to_string('k_akun/akun_manage_list.html',{'akunlist':akunlist},request=request)
    else:
        context = {
            'akun':akun
        }
        data['html_form'] = render_to_string('k_akun/partakundelete.html',context,request=request)
    
    return JsonResponse(data)

