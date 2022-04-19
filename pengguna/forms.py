from django import forms
from django.forms import EmailInput, TextInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Pengguna

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',

        ]
        labels = {
            'username':'Username',
            'email':'Email',
            'password1':'Password',
            'password2':'Confirm Password',
        }
        
        widgets = {
            'username':TextInput(
                attrs={
                    'placeholder':'Username',
                }
            ),
            'email':EmailInput(
                attrs={
                    'placeholder':'Ex : aaa@xxx.fff',
                }
            ),
        }

class PenggunaForm(forms.ModelForm):
    class Meta:
        model = Pengguna
        fields = '__all__'
        exclude = ['user']

