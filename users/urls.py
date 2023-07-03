from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path("", views.login, name="login"),
    path("home", views.home, name="home"),
    path("base/", views.base, name="base"),
    path("register/", views.register, name="register"),
    path(
        "logout/",
        auth.LogoutView.as_view(template_name="posts/login.html"),
        name="logout",
    ),
]
