from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

def unauthenticated_user(view_func):
    def wrapper_func(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func


def allowed_user(allowed_roles = []):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse(
                    '<script>alert("you dont have authorized for this page");window.location="'+str(reverse_lazy('dashboard'))+'";</script>'
                )
        return wrapper_func
    return decorator
