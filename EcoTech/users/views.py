from datetime import timedelta, timezone

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.decorators import login_required
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
                messages.success(request, 'Account created successfully!')
                return redirect('users:login')    # redirect to the user login page
            else:
                print('Invalid email or password')
                messages.error(request, 'Invalid email or password!')
                return redirect('users:signup')     # make sure to render a new empty form
        else:
            print('Form is not valid')
            messages.error(request, 'Form is not valid!')
            return redirect('users:signup')
    else:
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
                # request.session['last_login'] = str(timezone.now())
                # request.session.set_expiry(120)
                return redirect('contents:article_list')    # redirect to user dashboard later
            else:
                print(f"user: {username}, {password}")
                messages.error(request, 'Invalid email or password!')
                return redirect('users:login')
        else:
            print("Form is not valid")
            messages.error(request, 'Form is not valid!')
            return redirect('users:login')
    else:
        if request.user.is_authenticated:
            return redirect('contents:article_list')  # redirect to user dashboard later
        else:
            form = LoginForm()
            return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('core:home')


def password_forgot_view(request):
    if request.method == 'POST':
        form = PasswordForgotForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            try:
                member = get_object_or_404(Member, email=email)
                request.session['member_email'] = email
                return redirect('users:security_questions')
            except Exception:
                messages.error(request, 'The email does not exist.')
                return redirect('users:password_forgot')
        else:
            messages.error(request, 'Invalid email!')
            return redirect('users:password_forgot')
    else:
        form = PasswordForgotForm()
    return render(request, 'users/password_forgot.html', {'form': form})


def security_questions_view(request):
    email = request.session.get('member_email')
    member = get_object_or_404(Member, email=email)
    security_questions = SecurityQuestions.objects.get(member=member)

    question_1_text = security_questions.get_question_text(security_questions.security_question_1)
    question_2_text = security_questions.get_question_text(security_questions.security_question_2)
    question_3_text = security_questions.get_question_text(security_questions.security_question_3)

    print(question_1_text, question_2_text, question_3_text)

    context = {
        'question_1_text': question_1_text,
        'question_2_text': question_2_text,
        'question_3_text': question_3_text,
    }

    if request.method == 'POST':
        answer_1 = request.POST.get('security_answer_1')
        answer_2 = request.POST.get('security_answer_2')
        answer_3 = request.POST.get('security_answer_3')
        if (security_questions.security_answer_1 == answer_1 and
            security_questions.security_answer_2 == answer_2 and
            security_questions.security_answer_3 == answer_3):
            # Answers are correct, proceed to password reset
            return redirect('users:password_reset')
        else:
            messages.error(request, 'Security answers do not match.')

    return render(request, 'users/security_questions.html', context)


def password_reset_view(request):
    email = request.session.get('member_email')
    if not email:
        return redirect('users:password_forgot')    # display appropriate message as well

    member = get_object_or_404(get_user_model(), email=email)

    if request.method == 'POST':
        form = PasswordResetForm(member, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been reset successfully.')
            return redirect('users:password_reset_done')
        else:
            messages.error(request, 'Invalid password!')
    else:
        form = PasswordResetForm(member)

    return render(request, 'users/password_reset.html', {'form': form})


def password_reset_done_view(request):
    return render(request, 'users/password_reset_done.html')


def view_profile(request, username):
    user_profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'users/view_profile.html', {'user_profile': user_profile})


def edit_profile(request, username):
    user = get_object_or_404(Member, username=username)
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.username = request.POST.get('username')
            user.city = request.POST.get('city')
            user.country = request.POST.get('country')
            user.save()
            form.save()
            return redirect('users:view_profile', username=user.username)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'users/edit_profile.html', {'form': form, 'user_profile': user_profile})