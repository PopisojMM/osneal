from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Perfil

# Register your models here.

class PerfilInline(admin.StackedInline):
    model = Perfil

class CustomUserAdmin(UserAdmin):
    inlines = [PerfilInline,]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
