from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import LoginForm, RegistrationForm
from .models import Result, Test


class Login(LoginView):
    form_class = LoginForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('main:main')


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main:main')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main:main')


class Main(ListView):
    model = Test
    template_name = "main/main.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related('author', 'tasks')


class Test(DetailView):
    model = Test
    template_name = "main/test.html"


class Profile(ListView):
    model = Result
    template_name = "main/profile.html"

    def get_queryset(self):
        return super().get_queryset().filter(student__id=self.request.user.id).select_related('student', 'test')


def logout_user(request):
    logout(request)
    reverse_lazy
    return redirect('main:main')


def result(self, request):
    pass
