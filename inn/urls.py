"""inn URL Configuration

^accounts/password/reset/$ [name='rest_password_reset']
^accounts/password/reset/confirm/$ [name='rest_password_reset_confirm']
^accounts/login/$ [name='rest_login']
^accounts/logout/$ [name='rest_logout']
^accounts/user/$ [name='rest_user_details']
^accounts/password/change/$ [name='rest_password_change']
^accounts/signup/
^accounts/users/
^refresh-token/
"""
from django.conf.urls import url, include
from inn.api.accounts import views
from rest_framework_jwt.views import refresh_jwt_token
from allauth.account.views import confirm_email
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', views.Home, name="home"),
    url(r'^accounts/', include('rest_auth.urls')),
    url(r'^accounts/signup/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/$', refresh_jwt_token),
    url(r'^accounts/users/$', views.UserList.as_view(), name="users"),
    # url(r'^accounts/signup/account-confirm-email/(?P<key>.+)/$',
    url(r"^accounts/signup/account-confirm-email/(?P<key>[\s\d\w().+-_',:&]+)/$",
        TemplateView.as_view(template_name='confirm_mail.html'),
        confirm_email, name='account_confirm_email'),
]
