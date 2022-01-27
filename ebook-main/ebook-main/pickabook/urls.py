from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage),
    path('homepage', views.homepage),
    path('get_quote', views.get_quotes),
    path('quotes_form', views.Quote_Form),
    path('update_quote/<int:quote_id>', views.update_quotes),
    path('delete_quote/<int:quote_id>', views.delete_quote),
    path('category_form', views.category_form),
    path('get_category', views.get_category),
    path('update_category/<int:category_id>', views.update_category),
    path('delete_category/<int:category_id>', views.delete_category),
    path('books_form', views.books_form),
    path('get_books', views.get_books)
]