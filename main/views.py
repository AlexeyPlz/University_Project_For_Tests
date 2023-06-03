import json
from datetime import datetime

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import LoginForm, RegistrationForm
from .models import Answer, Result, ResultAnswer, Test


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
    template_name = 'main/main.html'
    context_object_name = 'tests'


class TestInfo(DetailView):
    model = Test
    template_name = 'main/test.html'


class Profile(ListView):
    model = Result
    template_name = 'main/profile.html'
    context_object_name = 'results'

    def get_queryset(self):
        return super().get_queryset().filter(student__id=self.request.user.id)


def logout_user(request):
    logout(request)
    return redirect('main:main')


def result(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        test = Test.objects.get(id=data['test_id'])
        del data['test_id']
        points = 0
        for answer_id in data.keys():
            answer = Answer.objects.get(id=answer_id)
            if answer.is_right:
                points += answer.point
        result = Result.objects.create(points=points, date = datetime.now(), test = test, student = request.user)
        for answer_id in data.keys():
            answer = Answer.objects.get(id=answer_id)
            ResultAnswer.objects.create(answer = answer, result = result)
    return redirect('main:main')
