from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import *
from .forms import *


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = MemberSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user:
                messages.success(request, 'Account created successfully')
                return redirect('core:home')    # will redirect to a user landing page later
    else:
        form = MemberSignUpForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('core:home')
            else:
                error_message = 'Invalid username or password!<br>Please try again!'
                return render(request, 'users/login.html', {'form': form, 'error': error_message})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('core:home')
