from django.urls import path
from django.views.generic import TemplateView

app_name = 'mascotas'

urlpatterns = [
    path('index/', TemplateView.as_view(template_name='index.html'),name='index'),
]
