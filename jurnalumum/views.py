from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

from .models import Jurnal
from .forms import JurnalForm

from pengguna.decorators import(
    allowed_user,
)
# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def manageJurnalUmum(request):
    tgl_jurnal = Jurnal.objects.values_list('tgl',flat=True).order_by('tgl').distinct()
    data_jurnal = Jurnal.objects.all()
    total_debet = 0
    total_kredit = 0
    for data in data_jurnal:
        if data.tipe == 'Debet':
            total_debet += data.nominal
        else:
            total_kredit += data.nominal
    
    context = {
        'page_title':'Jurnal Umum',
        'tgl_jurnal':tgl_jurnal,
        'total_debet':total_debet,
        'total_kredit':total_kredit,
    }
    return render(request, 'jurnal/jurnal_manage.html',context)

def save_jurnal_form(request,form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            tgl_jurnal = Jurnal.objects.values_list('tgl',flat=True).order_by('tgl').distinct()
            data_jurnal = Jurnal.objects.all()
            total_debet = 0
            total_kredit = 0
            for i in data_jurnal:
                if i.tipe == 'Debet':
                    total_debet += i.nominal
                else:
                    total_kredit += i.nominal
            
            context_data = {
                'tgl_jurnal':tgl_jurnal,
                'total_debet':total_debet,
                'total_kredit':total_kredit,
            }
            data['html_jurnal_list'] = render_to_string('jurnal/jurnal_manage_list.html',context_data)
        else:
            data['form_is_valid'] = False
    
    context = {
        'form':form,
    }
    data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def createJurnal(request):
    if request.method == 'POST':
        form = JurnalForm(request.POST)
    else:
        form = JurnalForm()
    
    return save_jurnal_form(request, form, 'jurnal/partjurnalcreate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def updateJurnal(request,pk):
    jurnal = Jurnal.objects.get(id=pk)
    if request.method == 'POST':
        form = JurnalForm(request.POST, instance=jurnal)
    else:
        form = JurnalForm(instance=jurnal)
    
    return save_jurnal_form(request, form, 'jurnal/partjurnalupdate.html')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['kasir','admin'])
def deleteJurnal(request, pk):
    data = dict()
    jurnal = Jurnal.objects.get(id=pk)
    if request.method == 'POST':
        jurnal.delete()
        data['form_is_valid'] = True
        tgl_jurnal = Jurnal.objects.values_list('tgl',flat=True).order_by('tgl').distinct()
        data_jurnal = Jurnal.objects.all()
        total_debet = 0
        total_kredit = 0
        for i in data_jurnal:
            if i.tipe == 'Debet':
                total_debet += i.nominal
            else:
                total_kredit += i.nominal
        
        context_data = {
            'tgl_jurnal':tgl_jurnal,
            'total_debet':total_debet,
            'total_kredit':total_kredit,
        }
        data['html_jurnal_list'] = render_to_string('jurnal/jurnal_manage_list.html',context_data,request=request)
    else:
        context = {
            'jurnal':jurnal,
        }
        data['html_form'] = render_to_string('jurnal/partjurnaldelete.html',context, request=request)
    
    return JsonResponse(data)

