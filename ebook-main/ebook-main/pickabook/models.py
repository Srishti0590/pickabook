from django.contrib.auth.models import User
from django.db import models
from django.core.validators import *
from django.core import validators


class Quotes(models.Model):
    objects = None
    quote_description = models.TextField(null=True)
    quote_author= models.CharField(max_length=500, null=True, validators=[validators.MinLengthValidator(2)])
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.quote_description


class Category(models.Model):
    category_name=models.CharField(max_length=200, null=True, validators=[validators.MinLengthValidator(2)])
    category_description= models.TextField()
    created_date= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.category_name


class Books(models.Model):
    objects = None
    book_title = models.CharField(max_length=500, null=True)
    book_image = models.ImageField(upload_to='static/uploads', null=True)
    book_pdf = models.FileField(upload_to='static/uploads', null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Book_title


class Book_detail(models.Model):
    objects = None
    book = models.ForeignKey(Books, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Book_ID



