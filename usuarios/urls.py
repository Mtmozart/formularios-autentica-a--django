from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import login, cadastro

urlpatterns = [
   path('login', login, name='login'),
   path('cadastro', cadastro, name='cadastro'),
] 