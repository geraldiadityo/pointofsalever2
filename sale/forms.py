from django import forms
from django.forms import Textarea,TextInput,NumberInput,HiddenInput

from .models import *

class SaleForm(forms.ModelForm):
    class Meta:
        model = SaleModel
        fields = [
            'invoice',
            'totalharga',
            'discount',
            'total_bayar',
            'cash',
            'kembalian',
            'note',
            'total_pendapatan',
        ]

        labels = {
            'invoice':'Invoice',
            'totalharga':'Total Harga',
            'discount':'Discount',
            'total_bayar':'Total Bayar',
            'kembalian':'Uang Kembalian',
            'note':'Note',
        }

        widgets = {
            'invoice':HiddenInput,
            'totalharga':NumberInput(
                attrs={
                    'placeholder':'Total Harga',
                    'value':'0',
                    'readonly':'readonly',
                }
            ),
            'discount':NumberInput(
                attrs={
                    'value':'0',
                    'min':'0',
                    'readonly':'readonly',
                }
            ),
            'cash':NumberInput(
                attrs={
                    'placeholder':'Uang Cash',
                    'value':'0',
                    'min':'0',
                }
            ),
            'kembalian':NumberInput(
                attrs={
                    'placeholder':'Uang Kembalian',
                    'readonly':'readonly',
                }
            ),
            'note':Textarea(
                attrs={
                    'cols':'30',
                    'rows':'4',
                }
            ),
            'total_pendapatan':HiddenInput
        }

class KeranjangForm(forms.ModelForm):
    class Meta:
        model = KeranjangModel
        fields = [
            'product',
            'qty',
            'discount',
            'totalharga',
        ]

        labels = {
            'product':'Product Name',
            'qty':'Quantity',
            'totalharga':'Total Harga',
        }

        widgets = {
            'product':HiddenInput,
            'qty':NumberInput(
                attrs={
                    'placeholder':'Quantity',
                }
            ),
            'discount':HiddenInput,
            'totalharga':HiddenInput,
        }