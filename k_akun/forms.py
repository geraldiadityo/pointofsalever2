from django import forms
from django.forms import TextInput, Select

from .models import Akun

class AkunForm(forms.ModelForm):
    class Meta:
        model = Akun
        fields = [
            'nama_akun',
            'kode_akun',
            'kategori',
        ]
        labels = {
            'nama_akun':'Nama Akun',
            'kode_akun':'Kode Akun',
            'kategori':'Kategori Akun',
        }
        
        widgets = {
            'nama_akun':TextInput,
            'kode_akun':TextInput,
            'kategori':Select,
        }

