from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class MemberSignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Member
        fields = ('email', 'name', 'password1', 'password2', 'city', 'country')
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
        )
        member = Member(user=user)
        if commit:
            user.save()
            member.save()
        return member

class LoginForm(forms.Form):
    username = forms.CharField(max_length =150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)