from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import *
from .forms import *


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            authenticated_member = authenticate(username=username, password=password)
            if authenticated_member:
                print('Account created successfully')
                messages.success(request, 'Account created successfully')
                return redirect('users:login')    # redirect to the user login page
            else:
                print('Invalid email or password')
                messages.error(request, 'Invalid email or password')
                form = SignUpForm()
                return render(request, 'users/signup.html', {'form': form, 'error_message': 'Invalid email or password'})
        else:
            print('Form is not valid')
            form = SignUpForm()
            return render(request, 'users/signup.html', {'form': form, 'error_message': 'Invalid email or password! Please try again'})
    else:
        print('refreshing')
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Attempting to authenticate user: {username}")
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('core:home')
            else:
                error_message = 'Invalid username or password!<br>Please try again!'
                print("Authentication failed: Invalid credentials")
                form = LoginForm()
                return render(request, 'users/login.html', {'form': form, 'error': error_message})
        else:
            print("Form is not valid")
            print(form.errors)
            form = LoginForm()
            return render(request, 'users/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('core:home')
