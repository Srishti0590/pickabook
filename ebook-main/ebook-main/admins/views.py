from django.shortcuts import render, redirect
from accounts.auth import admin_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import context

from pickabook.models import *
from django.contrib import messages


@admin_only
@login_required
def admin_dashboard(request):
    return render(request, 'admins/dashboard.html')


@login_required
@admin_only
def admin_dashboard(request):
    books = Books.objects.all()
    books_count = books.count()
    category = Category.objects.all()
    category_count = category.count()
    quote = Quotes.objects.all()
    quote_count = quote.count()
    user = User.objects.filter(is_staff=0)
    user_count = user.count()
    admin = User.objects.filter(is_staff=1)
    admin_count = admin.count()

    context ={
        'books': books_count,
        'category': category_count,
        'quote': quote_count,

        'user': user_count,
        'admin':admin_count
    }
    return render(request, 'admins/dashboard.html', context)

@login_required
@admin_only
def show_users(request):
    users = User.objects.filter(is_staff=0).order_by('-id')
    context = {
        'users': users
    }
    return render(request, 'admins/user.html', context)

@admin_only
@login_required
def delete_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'User Deleted Successfully')
    return redirect("admins/user.html")

@login_required
@admin_only
def show_admins(request):
    admins = User.objects.filter(is_staff=1).order_by('-id')
    context = {
        'admins': admins
    }
    return render(request, 'admins/admin.html', context)


@login_required
@admin_only
def promote_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_staff = True
    user.save()
    messages.add_message(request, messages.SUCCESS, 'User is successfully promoted to admin')
    return redirect('/admins/admins')


@login_required
@admin_only
def demote_admin(request, user_id):
    admin = User.objects.get(id=user_id)
    admin.is_staff = False
    admin.save()
    messages.add_message(request, messages.SUCCESS, 'Admin is demoted to user')
    return redirect('/admins/users')

