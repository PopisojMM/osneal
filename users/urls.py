from django.contrib import admin
from django.urls import path
from .views import Login

app_name = 'users'

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
]
