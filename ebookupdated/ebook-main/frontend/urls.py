from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.homepage, name='my_homepage'),
    path('quotes', views.show_quotes),
    path('explore', views.all_books),
    path('recommend', views.recommend),
    path('genres', views.show_categories),
    path('books/<int:category_id>', views.show_books),
    path('book', views.book_detail),
    path('news', views.show_news),
    path('writings', views.writing_form),

    path('esewa_verify', views.esewa_verify)
]