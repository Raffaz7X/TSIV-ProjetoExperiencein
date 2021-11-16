from django.urls import include, path
from django.contrib import admin
from perfis import views


urlpatterns = [
	path('', views.index, name='index'),
	path('perfis/<int:perfil_id>', views.exibir, name='exibir'),
	path('perfis/<int:perfil_id>/convidar', views.convidar, name='convidar')
]