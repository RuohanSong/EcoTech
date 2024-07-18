from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout

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
    if request.user.is_authenticated:
        return redirect('core:home')    # redirect to user dashboard later

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(f"Attempting to authenticate user: {username}")
            authenticated_user = authenticate(request, username=username, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('core:home')    # redirect to user dashboard later
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


def password_forgot_view(request):
    if request.method == 'POST':
        form = PasswordForgotForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            member = get_object_or_404(Member, email=email)
            request.session['member_email'] = email
            return redirect('users:security_questions')
        else:
            messages.error(request, 'Invalid email!')
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