from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import LoginForm, RegistrationForm
from .models import Test


class Login(LoginView):
    form_class = LoginForm
    template_name = 'main/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('main:main')


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)


class Main(ListView):
    model = Test
    template_name = "main/main.html"
