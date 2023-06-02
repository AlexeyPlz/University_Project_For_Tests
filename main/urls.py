from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Registration.as_view(), name='register'),
]
