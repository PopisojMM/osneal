from django.urls import path,re_path
from django.views.generic import TemplateView
from .views import (
    UserLoginView,
    UserLogoutView,
    CrearUsuarioView,
    json_buscar_usuario,
    BuscarUsuarioView,
    EditarUsuarioView,
    BorrarUsuarioView,
    UsuarioAutocomplete,
    )


app_name='usuarios'

urlpatterns = [
    # path('crear_usuario/', crear_usario,name='crear_usuario'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', UserLogoutView.as_view(),name='logout'),
    path('crear_usuario/', CrearUsuarioView.as_view(),name='crear_usuario'),
    path('json_buscar_usuario/<dni>', json_buscar_usuario,name='json_buscar_usuario'),
    path('buscar_usuario/', BuscarUsuarioView.as_view(),name='buscar_usuario'),
    path('<int:pk>/editar_usuario/', EditarUsuarioView.as_view(),name='editar_usuario'),
    path('<int:pk>/borrar_usuario/', BorrarUsuarioView.as_view(),name='borrar_usuario'),
    re_path(
        r'^usuario-autocomplete/$',
        UsuarioAutocomplete.as_view(),
        name='usuario-autocomplete',
    ),

]


