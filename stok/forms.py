from django import forms
from django.forms import Select,TextInput,Textarea,NumberInput,DateInput

from .models import StokM

class StokInForm(forms.ModelForm):
    class Meta:
        model = StokM
        fields = [
            'product',
            'tipe',
            'detail',
            'supplier',
            'hargabeli',
            'qty',
            'total',
            'expired_date',
        ]

        labels = {
            'product':'Nama Product',
            'tipe':'Type Stok',
            'detail':'Detail Stok',
            'supplier':'Supplier',
            'hargabeli':'Harga Beli',
            'qty':'Banyak Kuantitas',
            'total':'Total',
            'expired_date':'Tanggal Expired'
        }

        widgets = {
            'product':Select,
            'tipe':TextInput(
                attrs={
                    'type':'hidden',
                }
            ),
            'detail':Textarea(
                attrs={
                    'cols':'30',
                    'rows':'4',
                }
            ),
            'supplier':Select,
            'hargabeli':NumberInput,
            'qty':NumberInput(
                attrs={
                    'placeholder':'Banyak Quantity',
                }
            ),
            'total':NumberInput,
            'expired_date':DateInput(
                attrs={
                    'type':'date',
                }
            ),
        }

class StokOutForm(forms.ModelForm):
    class Meta:
        model = StokM
        fields = [
            'product',
            'tipe',
            'detail',
            'hargabeli',
            'qty',
            'total',
        ]

        labels = {
            'product':'Nama Product',
            'tipe':'Type Stok',
            'detail':'Detail Stok',
            'hargabeli':'Harga Beli',
            'qty':'Banyak Kuantitas',
            'total':'Total',
        }

        widgets = {
            'product':Select,
            'tipe':TextInput(
                attrs={
                    'type':'hidden',
                }
            ),
            'detail':Textarea(
                attrs={
                    'cols':'30',
                    'rows':'4',
                }
            ),
            'qty':NumberInput,
            'hargabeli':NumberInput,
            'total':NumberInput,
        }