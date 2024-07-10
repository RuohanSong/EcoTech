from django import forms
from django.contrib.auth.models import User
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length =150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)