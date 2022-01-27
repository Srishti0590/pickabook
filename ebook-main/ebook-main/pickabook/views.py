from django.contrib import messages
from django.shortcuts import render, redirect

from accounts.auth import unauthenticated_user
from .forms import QuoteForm, CategoryForm, BooksForm
# from django.contrib import messages
from .models import Quotes,Category, Books
from accounts.auth import unauthenticated_user, admin_only, user_only

from django.contrib.auth.decorators import login_required
import os
# from .article_filter import ArticleFilter


#@unauthenticated_user
def homepage(request):
    return render(request, 'pickabook/homepage.html')


@admin_only
def Quote_Form(request):
    if request.method == "POST":
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Quote added succesfully")
            return redirect("/pickabook/get_quote")
        else:
            messages.add_message(request, messages.ERROR, "unable to add Quote")
            return render(request, 'pickabook/Quote_Form.html', {'form_quote': form})
    context = {
        'form_quote': QuoteForm,
        'activate_quote': 'active'
    }
    return render(request, 'pickabook/Quote_Form.html', context)


@admin_only
def get_quotes(request):
    quotes= Quotes.objects.all().order_by('-id')
    context={
        'quotes':quotes,
        'activate_quotes': 'active'
    }
    return render(request, 'pickabook/get_quotes.html', context)


@admin_only
def update_quotes(request, quote_id):
    quote = Quotes.objects.get(id=quote_id)
    if request.method == "POST":
        form = QuoteForm(request.POST, request.FILES, instance=quote)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "category updated succesfully")
            return redirect("/pickabook/get_quote")
        else:
            messages.add_message(request, messages.ERROR, "unable to update category")
            return render(request, 'pickabook/Quote_Form.html', {'form_category': form})
    context = {
        'form_quote': QuoteForm(instance=quote),
        'activate_quote': 'active'
    }
    return render(request, 'pickabook/update_quotes.html', context)


@admin_only
def delete_quote(request, quote_id):
    quote = Quotes.objects.get(id=quote_id)
    quote.delete()
    messages.add_message(request, messages.SUCCESS, 'Quote Deleted Succesfully')
    return redirect("/pickabook/get_quote")


@admin_only
def category_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "category added succesfully")
            return redirect("/pickabook/get_category")
        else:
            messages.add_message(request, messages.ERROR, "unable to add category")
            return render(request, 'pickabook/category_form.html', {'form_category': form})
    context = {
        'form_category': CategoryForm,
        'activate_category': 'active'
    }
    return render(request, 'pickabook/category_form.html', context)

@admin_only
def get_category(request):
    categories= Category.objects.all().order_by('-id')
    context={
        'categories':categories,
        'activate_category': 'active'
    }
    return render(request, 'pickabook/get_category.html', context)



@admin_only
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "category updated succesfully")
            return redirect("/pickabook/get_category")
        else:
            messages.add_message(request, messages.ERROR, "unable to update category")
            return render(request, 'pickabook/category_form.html', {'form_category': form})
    context = {
        'form_category': CategoryForm(instance=category),
        'activate_category': 'active'
    }
    return render(request, 'pickabook/update_category.html', context)


@admin_only
def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request, messages.SUCCESS, 'Category Deleted Succesfully')
    return redirect("/pickabook/get_category")


@admin_only
def books_form(request):
    if request.method=="POST":
        form = BooksForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Book added succesfully")
            return redirect("/pickabook/get_books")
        else:
            messages.add_message(request, messages.ERROR, "unable to add Book")
            return render(request, 'pickabook/books_form.html', {'form_book': form})
    context = {
        'form_book': BooksForm,
        'activate_book': 'active'
    }

    return render(request, 'pickabook/books_form.html', context)

@admin_only
def get_books(request):
    book= Books.objects.all().order_by('-id')
    context={
        'book':book,
        'activate_book': 'active'
    }
    return render(request, 'pickabook/get_books.html', context)


