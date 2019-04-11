
from django.conf.urls import url
from api.accounts import views
from rest_auth import views as auth_views
from rest_auth.registration.views import RegisterView, VerifyEmailView
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns
from allauth.account.views import ConfirmEmailView
from api.story.views import CreateViewStory, ViewStory
from api.comments.views import CreateViewComment, ViewComment
from django.urls import include, re-path

urlpatterns = [
    url(r'^$', views.Home, name="home"),

    url(r'^api/v1/auth/password/reset/$', auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    url(r'^api/v1/auth/password/reset/confirm/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='confirm_account_logout'),
    url(r'^api/v1/auth/login/$', auth_views.LoginView.as_view(),
        name='account_login'),
    url(r'^api/v1/auth/logout/$', auth_views.LogoutView.as_view(),
        name='account_logout'),
    url(r'^accounts/user/$', auth_views.UserDetailsView.as_view(),
        name='account_user'),
    url(r'^api/v1/auth/password/change/$',
        auth_views.PasswordChangeView.as_view(),
        name='password_change'),

    url(r'^api/v1/auth/signup/', RegisterView.as_view(), name='account_signup'),
    url(r'^refresh-token/$', refresh_jwt_token),
    url(r'^accounts/users/$', views.UserList.as_view(), name="users"),
    url(r'^accounts/verify-email/$', VerifyEmailView.as_view(),
        name='rest_verify_email'),
    url(r'^accounts/confirmemail/(?P<key>[-:\w]+)/$',
        ConfirmEmailView.as_view(),
        name='account_confirm_email'),
    url(r'^api/v1/story/$', CreateViewStory.as_view(), name='create_story'),
    url(r'^api/v1/story/(?P<pk>[0-9]+)/$', ViewStory.as_view(), name='view_story'),

    path("api/v1/comment/$", CreateViewComment.as_view(), name='create_comment'),
    path("api/v1/comment/<int: pk>", ViewComment.as_view(), name='view_comment'),
]
