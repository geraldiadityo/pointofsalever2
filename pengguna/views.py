from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Pengguna

from .decorators import (
    allowed_user,
    unauthenticated_user,
)

from .forms import (
    CreateUserForm,
    PenggunaForm,
)


# Create your views here.
@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin','penulis'])
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return HttpResponse(
                '<script>alert("registrasi dengan username '+str(username)+'");window.location="'+str(reverse_lazy('pengguna:manage'))+'";</script>'
            )
    context = {
        'form':form,
        'page_title':'Registrasi Akun Pengguna',
    }
    return render(request, 'pengguna/create_pengguna.html',context)

@unauthenticated_user
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse(
                '<script>alert("username and password combination is wrong, try again");window.location="'+str(reverse_lazy('pengguna:login'))+'";</script>'
            )
    context = {}
    return render(request, 'pengguna/login.html',context)

@login_required(login_url='pengguna:login')
def logoutView(request):
    logout(request)
    return redirect('pengguna:login')

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def managePengguna(request):
    penggunaList = Pengguna.objects.all().order_by('-date_create')
    context = {
        'page_title':'Manage Pengguna',
        'pengguna':penggunaList,
    }
    return render(request, 'pengguna/manage_pengguna.html',context)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def viewPengguna(request,pk):
    pengguna = Pengguna.objects.get(id=pk)
    role = User.objects.get(id=pk).groups.all()[0].name
    data = dict()
    context = {
        'pengguna':pengguna,
        'role':role,
    }
    data['html_form'] = render_to_string('pengguna/view_pengguna.html',context,request=request)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
@allowed_user(allowed_roles=['admin'])
def deletePengguna(request,pk):
    pengguna = Pengguna.objects.get(id=pk)
    data = dict()
    if request.method == 'POST':
        pengguna.delete()
        data['form_is_valid'] = True
        penggunaList = Pengguna.objects.all().order_by('-date_created')
        data['html_pengguna_list'] = render_to_string('pengguna/manage_pengguna_list.html',{'pengguna':penggunaList},request=request)
    else:
        context = {
            'pengguna':pengguna,
        }
        data['html_form'] = render_to_string('pengguna/partpenggunadelete.html',context,request=request)
    return JsonResponse(data)

@login_required(login_url='pengguna:login')
def editProfilePengguna(request):
    pengguna = Pengguna.objects.get(id=request.user.pengguna.id)
    form = PenggunaForm(instance=pengguna)
    if request.method == 'POST':
        form = PenggunaForm(request.POST,request.FILES,instance=pengguna)
        if form.is_valid():
            form.save()
            return HttpResponse(
                '<script>alert("profile success update");window.location="'+str(reverse_lazy('dashboard'))+'";</script>'
            )
    context = {
        'page_title':'Profile Setting',
        'form':form,
    }
    return render(request, 'pengguna/profile_setting.html',context)

