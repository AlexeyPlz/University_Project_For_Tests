from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'content', 'placeholder': 'Логин *'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'content', 'placeholder': 'Пароль *'}))


class RegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'content', 'placeholder': 'Логин *'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'content', 'placeholder': 'Почта *'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'content', 'placeholder': 'Пароль *'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'content', 'placeholder': 'Повторите пароль *'}))
