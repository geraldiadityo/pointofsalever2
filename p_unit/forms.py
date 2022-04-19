from django import forms
from django.forms import TextInput

from .models import Unit_p

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit_p
        fields = [
            'nama',
        ]
        labels = {
            'nama':'Nama Unit',
        }
        
        widgets = {
            'nama':TextInput(
                attrs={
                    'placeholder':'Nama Unit',
                }
            ),
        }
        