from django import forms
from django.forms import ModelForm
from .models import Quotes, Category, Books


class QuoteForm(ModelForm):
    class Meta:
        model= Quotes
        fields = "__all__"


class CategoryForm(ModelForm):
    class Meta:
        model= Category
        fields = "__all__"


class BooksForm(ModelForm):
    class Meta:
        model= Books
        fields= "__all__"

