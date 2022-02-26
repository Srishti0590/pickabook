from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages, auth

from accounts.auth import unauthenticated_user, admin_only, user_only
from django.contrib.auth.decorators import login_required

from accounts.forms import RegisterForm, ProfileForm, ContactusForm
from .models import Profile


# @user_only
# def homepage(request):
#     context = {
#         "activate_home": 'active'
#     }
#     return render(request, 'accounts/homepage.html', context)


@unauthenticated_user
def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passwd = request.POST['password']
        user = auth.authenticate(username=uname, password=passwd)
        if user is not None:
            if not user.is_staff:
                auth.login(request, user)
                messages.success(request,"Welcome to Ebook")
                return redirect("/pickabook/home")
            elif user.is_staff:
                auth.login(request, user)
                return redirect('/admins/dashboard')
        else:
            messages.add_message(request, messages.ERROR, "Invalid Username and Password!")
            return render(request, 'accounts/login.html' )
    else:
        return render(request, 'accounts/login.html')
    context = {

    }
    return render(request, 'accounts/login.html', context)


@unauthenticated_user
def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            Profile.objects.create(user=user, username=user.username)
            messages.add_message(request, messages.SUCCESS, 'User registered successfully')
            return redirect('/accounts/login')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to register User')
            return render(request, 'accounts/register.html', {'form':form})

    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('/accounts/login')


@login_required
@user_only
def password_change_user(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.add_message(request, messages.SUCCESS, 'Password has been changed Successfully')
            return redirect('/accounts/password_change_user')
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'accounts/password_change_user.html', {'password_change_form': form})

    context = {
        'password_change_form': PasswordChangeForm(request.user),
        'activate_password': 'active'
    }
    return render(request, 'accounts/password_change_user.html', context)


@login_required
@user_only
def profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile Updated Successfully")
            return redirect('/accounts/profile')
    context = {
        'form': ProfileForm(instance=profile),
        'activate_profile': 'active'
    }
    return render(request, 'accounts/profile.html', context)

def contactus(request):
    context = {
        'form': ContactusForm,
    }
    if request.method == "POST":
        form = ContactusForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Sent Successfully")
            return redirect("/accounts/contactus")

        else:
            messages.add_message(request, messages.ERROR, 'Contact form is not added')
    return render(request, 'accounts/contactus.html', context)
