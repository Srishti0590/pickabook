from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('pickabook.urls')),
    path('accounts/', include('accounts.urls')),
    path('pickabook/', include('pickabook.urls')),
    path('admins/', include('admins.urls')),
    path('pickabook/', include('frontend.urls')),
    # path('quiz/', include('Quiz.urls'))
]
