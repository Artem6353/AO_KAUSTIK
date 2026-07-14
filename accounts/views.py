from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm, RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect("main:index")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect("main:index")
        else:
            messages.error(request, "Некорректный логин или пароль.")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из системы.")
    return redirect("main:index")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("main:index")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "customer"
            user.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect("main:index")
        else:
            messages.error(request, "Исправьте ошибки в форме.")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})
