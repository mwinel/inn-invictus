"""inn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
# from django.contrib import admin
# from api.accounts import views
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token

# urlpatterns = [
#     url(r"^admin/", admin.site.urls),
#     url(r"^api/token/", obtain_jwt_token),
#     url(r"^api/token/refresh/", refresh_jwt_token),
#     url(r"^api/token/verify/", verify_jwt_token),
#     url(r"^hello/", views.HelloView.as_view(), name="hello"),
#     url(r"^accounts/profile/<int:pk>", views.UserDetail.as_view(), name="user"),
#     url(r"^accounts/users/", views.UserList.as_view(), name="users"),
#     url(r"^accounts/login/", views.Login.as_view(), name="login"),
#     url(r"^accounts/signup/", views.SignUp.as_view(), name="signup"),
# ]

from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
]
