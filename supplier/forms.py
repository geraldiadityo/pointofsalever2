from django import forms
from django.forms import TextInput, Textarea, NumberInput
from .models import Supplier

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = [
            'nama',
            'telp',
            'alamat',
            'deskripsi',
        ]
        widgets = {
            'nama':TextInput(
                attrs={
                    'placeholder':'Nama Supplier',
                }
            ),
            'telp':NumberInput(
                attrs={
                    'placeholder':'No Telp',
                }
            ),
            'alamat':Textarea(
                attrs={
                    'cols':'30',
                    'rows':'5',
                }
            ),
            'deskripsi':Textarea(
                attrs={
                    'cols':'10',
                    'rows':'5'
                }
            ),
        }

        labels = {
            'nama':'Nama Supplier',
            'telp':'No Telp',
            'alamat':'Alamat Supplier',
            'deskripsi':'Deskripsi/ Catatan',
        }
