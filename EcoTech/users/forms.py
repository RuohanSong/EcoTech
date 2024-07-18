from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm
from django.contrib.auth.hashers import make_password
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

    QUESTION_CHOICES = [
        ('q1', 'What is your favorite color?'),
        ('q2', 'What is your mother\'s first name?'),
        ('q3', 'What was the name of your first pet?')
    ]

    security_question_1 = forms.ChoiceField(choices=QUESTION_CHOICES, required=True, label="Security Question 1")
    security_answer_1 = forms.CharField(required=True, label="Answer to Security Question 1")
    security_question_2 = forms.ChoiceField(choices=QUESTION_CHOICES, required=True, label="Security Question 2")
    security_answer_2 = forms.CharField(required=True, label="Answer to Security Question 2")
    security_question_3 = forms.ChoiceField(choices=QUESTION_CHOICES, required=True, label="Security Question 3")
    security_answer_3 = forms.CharField(required=True, label="Answer to Security Question 3")

    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'city', 'country')

    def save(self, commit=True):
        member = super().save(commit=False)
        member.email = self.cleaned_data['username']  # save member's email as well
        if commit:
            member.save()
            security_questions = SecurityQuestions(
                member=member,
                security_question_1=self.cleaned_data['security_question_1'],
                security_answer_1=self.cleaned_data['security_answer_1'],
                security_question_2=self.cleaned_data['security_question_2'],
                security_answer_2=self.cleaned_data['security_answer_2'],
                security_question_3=self.cleaned_data['security_question_3'],
                security_answer_3=self.cleaned_data['security_answer_3'],
            )
            security_questions.save()
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


class PasswordForgotForm(forms.Form):
    email = forms.EmailField(required=True, label="Email")


# class SecurityQuestionForm(forms.Form):
#     security_answer_1 = forms.CharField(required=True, label=Member.objects.get(email=email).security_question_1)
#     security_answer_2 = forms.CharField(required=True, label=Member.objects.get(email=email).security_question_1)
#     security_answer_3 = forms.CharField(required=True, label=Member.objects.get(email=email).security_question_1)


class PasswordResetForm(SetPasswordForm):
    new_password1 = forms.CharField(
        required=True,
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'})
    )
    new_password2 = forms.CharField(
        required=True,
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'})
    )

    class Meta:
        model = get_user_model()
        fields = ('new_password1', 'new_password2')


# forms.py

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_pic']