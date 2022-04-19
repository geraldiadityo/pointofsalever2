from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import Kategori_p
from .forms import KategoriForm
from pengguna.decorators import (
    allowed_user,
)

# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def kategoriManage(request):
    kategoris = Kategori_p.objects.all()
    context = {
        'page_title':'Kategori Product',
        'kategori':kategoris,
    }
    return render(request, 'p_kategori/kategori_manage.html',context)

def kategori_save_form(request,form,template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            kategoris = Kategori_p.objects.all()
            data['html_kategori_list'] = render_to_string('p_kategori/kategori_manage_list.html',{'kategori':kategoris})
        else:
            data['form_is_valid'] = False
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context,request = request)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def createKategori(request):
    if request.method == 'POST':
        form = KategoriForm(request.POST)
    else:
        form = KategoriForm()
    return kategori_save_form(request, form, 'p_kategori/partkategoricreate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def updateKategori(request,pk):
    kategori = Kategori_p.objects.get(id=pk)
    if request.method == 'POST':
        form = KategoriForm(request.POST,instance=kategori)
    else:
        form = KategoriForm(instance=kategori)
    return kategori_save_form(request, form, 'p_kategori/partkategoriupdate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def deleteKategori(request,pk):
    kategori = Kategori_p.objects.get(id=pk)
    data = dict()
    if request.method == 'POST':
        kategori.delete()
        data['form_is_valid'] = True
        kategoris = Kategori_p.objects.all()
        data['html_kategori_list'] = render_to_string('p_kategori/kategori_manage_list.html',{'kategori':kategoris},request=request)
    else:
        context = {
            'kategori':kategori,
        }
        data['html_form'] = render_to_string('p_kategori/partkategoridelete.html',context, request=request)
    return JsonResponse(data)



