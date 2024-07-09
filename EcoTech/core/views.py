
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Home page view- will load the default landing page
def home_view(request):
    return render(request, 'core/home.html')



#About Us view- Will load the page for About Us
def about_view(request):
    return render(request, 'core/about.html')


def faq_view(request):
  return render(request, 'core/FAQ.html')


def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)  # Log the user in after successful signup
      return redirect('home')  # Redirect to the home page after signup
  else:
    form = UserCreationForm()
  return render(request, 'core/signup.html', {'form': form})
