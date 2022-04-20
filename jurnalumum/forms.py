from django import forms
from django.forms import NumberInput,TextInput,Select,DateInput

from .models import Jurnal

class JurnalForm(forms.ModelForm):
    class Meta:
        model = Jurnal
        fields = [
            'tgl',
            'akun',
            'ket',
            'ref',
            'nominal',
            'tipe',
        ]

        labels = {
            'tgl':'Tanggal Transaksi',
            'akun':'Akun Transaksi',
            'ket':'Keterangan',
            'ref':'Referensi',
            'nominal':'Nominal Uang',
            'tipe':'Tipe Transaksi',
        }

        widgets = {
            'tgl':DateInput(
                attrs={
                    'type':'date',
                }
            ),
            'akun':Select,
            'ket':TextInput,
            'ref':TextInput,
            'nominal':NumberInput,
            'tipe':Select,
        }

