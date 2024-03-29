from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, \
    PasswordChangeView, PasswordChangeDoneView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='registration/logged_out.html'),
        name='logout'
    ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path(
        'login/',
        LoginView.as_view(template_name='registration/login.html'),
        name='login'
    ),
    path(
        'password_reset/',
        PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ),
        name='password_reset'
    ),
    # path(
    #     'password_change/',
    #     PasswordChangeView.as_view(
    #         template_name='registration/password_change_form.html'
    #     ),
    #     name='password_change'
    # ),
    # path(
    #     'password_change/done/',
    #     PasswordChangeDoneView.as_view(
    #         template_name='registration/password_change_done.html'
    #     ),
    #     name='password_change_done'
    # ),
    # path(
    #     'password_reset/done/',
    #     PasswordResetDoneView.as_view(
    #         template_name='registration/password_reset_done.html'
    #     ),
    #     name='password_reset_done'
    # ),
    # path(
    #     'reset/<uidb64>/<token>/',
    #     PasswordResetConfirmView.as_view(
    #         template_name='registration/password_reset_confirm.html'
    #     ),
    #     name='password_reset_confirm'
    # ),
    # path(
    #     'reset/done/',
    #     PasswordResetCompleteView.as_view(
    #         template_name='registration/password_reset_complete.html'
    #     ),
    #     name='password_reset_complete'
    # ),
]

