from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Registration.as_view(), name='register'),
    path('logout', login_required(views.logout_user), name='logout'),
    path('profile', login_required(views.Profile.as_view()), name='profile'),
    path('test/<int:pk>/', login_required(views.Test.as_view()), name='test'),
    path('result', login_required(views.result), name='result'),
]
