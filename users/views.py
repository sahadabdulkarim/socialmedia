from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import UserRegisterForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from feed.models import Post


def base(request):
    return render(request, "users/base.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            auth_login(request, new_user)
            return redirect("login")

    else:
        form = UserRegisterForm()

    context = {"form": form}

    return render(request, "users/register.html", context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect("home")

    else:
        form = AuthenticationForm()

    context = {"form": form}

    return render(request, "users/login.html", context)


@login_required
def home(request):
    post = Post.objects.all()

    context = {"post": post}
    return render(request, "home/home.html", context)
