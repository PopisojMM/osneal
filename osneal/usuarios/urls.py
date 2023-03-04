from django.urls import path,include
from django.views.generic import TemplateView
from .views import UserLoginView,UserLogoutView


app_name='usuarios'

urlpatterns = [
    path('alta-propietarios/', TemplateView.as_view(template_name='usuarios/alta-propietarios.html'),name='alta-propietarios'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', UserLogoutView.as_view(),name='logout'),
]
