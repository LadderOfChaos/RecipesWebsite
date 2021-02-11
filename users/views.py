from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from RecepiesSite.forms.email_sub_form import EmailSignupForm
from users.forms import RegisterForm, UserProfileForm
from django.contrib import messages

from users.models import UserProfile


def register(request):
    form = EmailSignupForm()
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            profile = UserProfile(user=user, )
            profile.save()
            login(request, user)
            username = reg_form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('index')
    else:
        reg_form = RegisterForm()
    context = {
        'reg_form': reg_form,
        'form': form,
    }
    return render(request, 'users/register.html', context)


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'profile_form': UserProfileForm(),
            'e_form': EmailSignupForm(),
        }

        return render(request, 'users/profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')


def signout_user(request):
    logout(request)
    return redirect('index')




