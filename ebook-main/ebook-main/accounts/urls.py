from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.homepage),
    path('login', views.login),
    path('register', views.register_user),
    path('logout', views.logout_user),


    path('password_change', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html')),
    path('password_change_done', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change_done.html'), name='password_change_done'),

    path('password_change_user', views.password_change_user),



#forgot password urls

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),


]