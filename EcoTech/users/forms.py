from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import *
import json


class SignUpForm(UserCreationForm):
    username = forms.EmailField(
        required=True,
        max_length=150,
        label="Email",  # make user to input an email as the username
    )
    city = forms.CharField(required=False)
    country = forms.CharField(required=False)

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'city', 'country')

    def save(self, commit=True):
        member = super().save(commit=False)
        member.email = self.cleaned_data['username']  # save member's email as well
        if commit:
            member.save()
            return member


class LoginForm(forms.Form):
    username = forms.EmailField(
        max_length=150,
        required=True,
        label="Email",  # make user to input an email as the username
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )


# forms.py

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic']