from django.urls import path,include
from django.views.generic import TemplateView
from .views import UserLoginView,UserLogoutView


app_name='usuarios'

urlpatterns = [
    # path('crear_usuario/', crear_usario,name='crear_usuario'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', UserLogoutView.as_view(),name='logout'),
]

