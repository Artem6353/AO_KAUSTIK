from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"placeholder": "Логин", "autocomplete": "off"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"placeholder": "••••••", "autocomplete": "off"}),
    )


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1", "password2")
