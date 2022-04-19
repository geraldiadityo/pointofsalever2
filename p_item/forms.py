from django import forms
from django.forms import TextInput,Select,NumberInput,DateInput
from .models import Item_p

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item_p
        fields = [
            'barcode',
            'nama',
            'kategori',
            'unit',

        ]

        labels = {
            'barcode':'Barcode Item',
            'nama':'Nama Item',
            'kategori':'Kategori Item',
            'unit':'Unit Item',
        }

        widgets = {
            'barcode':TextInput(
                attrs={
                    'placeholder':'BARCODE',
                }
            ),
            'nama':TextInput(
                attrs={
                    'placeholder':'Nama Item',
                }
            ),
            'kategori':Select,
            'unit':Select,
        }