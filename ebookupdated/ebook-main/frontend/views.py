from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.db.models import Q


from accounts.auth import user_only
from pickabook.models import Quotes, Category, Books, News


@login_required
@user_only
def homepage(request):
    context = {
        'activate_homepage': 'active'
    }
    return render(request, 'frontend/homepage.html', context)


def show_quotes(request):
    quotes = Quotes.objects.all().order_by('-id')
    context={
        'quotes': quotes,
        'activate_quotes_user': 'active'
    }
    return render(request, 'frontend/show_quotes.html', context)


def show_categories(request):
    categories= Category.objects.all().order_by('-id')
    context={
        'categories':categories,
        'activate_category': 'active'
    }
    return render(request, 'frontend/show_categories.html', context)


def show_books(request, category_id):
    category = Category.objects.get(id=category_id)
    context = {
        'category': category,
        'activate_book': 'active'
    }
    return render(request, 'frontend/show_books.html', context)


def all_books(request):
    book = Books.objects.all().order_by('-id')
    context = {
        'book': book,
        'activate_book': 'active'
    }
    return render(request, 'frontend/all_books.html', context)


def recommend(request):
    book = Books.objects.filter(Q(book_author="Paulo Coelho") | Q(book_author="Louisa May Alcott (1832-1888)"))
    context = {
        'book': book,
        'activate_book': 'active'
    }
    return render(request, 'frontend/all_books.html', context)


def book_detail(request, ):
    book = Books.objects.get
    context = {
        'book': book,
        'activate_book_detail': 'active'
    }
    return render(request, 'frontend/book_detail.html', context)


def show_news(request):
    news = News.objects.all().order_by('-id')
    context = {
        'news': news,
        'activate_news': 'active'
    }
    return render(request, 'frontend/show_news.html', context)

@user_only
@login_required
def writing_form(request):
    if request.method == "POST":
        form = WritingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Thank you for sharing your creativity")
            return redirect("/frontend/writings")
        else:
            messages.add_message(request, messages.ERROR, "Sorry, an error occurred. Please try again later")
            return render(request, 'frontend/writing.html', {'form_writing': form})
    context = {
        'form_writing': WritingForm,
        'activate_writing': 'active'
    }
    return render(request, 'frontend/writing.html', context)





import requests as req
def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id = request.GET.get('oid')
    amount = request.GET.get('amt')
    refId = request.GET.get('refId')
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amount,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid': o_id,
    }
    resp = req.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        order_id = o_id.split("_")[0]
        order = Order.objects.get(id=order_id)
        order.payment_status = True
        order.save()
        cart_id = o_id.split("_")[1]
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request, messages.SUCCESS, 'Payment Successful')
        return redirect('/accounts/homepage')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to make payment')
        return redirect('/accounts/homepage')

