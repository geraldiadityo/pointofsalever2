from django import forms
from django.forms import TextInput

from .models import Kategori_p

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori_p
        fields = [
            'nama',
        ]
        
        labels = {
            'nama':'Nama Kategori',
        }
        
        widgets = {
            'nama':TextInput(
                attrs={
                    'placeholder':'Nama Kategori',
                }
            ),
        }

