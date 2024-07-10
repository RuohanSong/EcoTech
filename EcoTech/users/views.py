from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import *


# Create your views here.
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
