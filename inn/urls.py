
from django.conf.urls import url
from . import views
from rest_auth import views as auth_views
from rest_auth.registration.views import RegisterView, VerifyEmailView
from rest_framework_jwt.views import refresh_jwt_token
from allauth.account.views import ConfirmEmailView

urlpatterns = [
    url(r'^$', views.Home, name="home"),

    url(r'^accounts/password/reset/$', auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^accounts/password/reset/confirm/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='confirm_account_logout'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(),
        name='account_login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(),
        name='account_logout'),
    url(r'^accounts/user/$', auth_views.UserDetailsView.as_view(),
        name='account_user'),
    url(r'^accounts/password/change/$', auth_views.PasswordChangeView.as_view(),
        name='password_change'),

    url(r'^accounts/signup/', RegisterView.as_view(), name='account_signup'),
    url(r'^refresh-token/$', refresh_jwt_token),
    url(r'^accounts/users/$', views.UserList.as_view(), name="users"),
    url(r'^accounts/verify-email/$', VerifyEmailView.as_view(),
        name='rest_verify_email'),
    url(r'^accounts/account-confirm-email/(?P<key>[-:\w]+)/$',
        ConfirmEmailView.as_view(),
        name='account_confirm_email'),
]
