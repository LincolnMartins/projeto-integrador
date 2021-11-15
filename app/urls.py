from django.urls import path
from . import views

urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='nome-da-url'),
    path('', views.logar, name='home'),
    path('registro/', views.cadastrarusuario, name='registro'),
    path('dashboard/', views.listaordem, name='listaordem'),
    path('cliente/', views.listacliente, name='cliente'),
    path('cadastrocliente/', views.cadastrocliente, name='cadastrocliente'),
    path('atualizacliente/<str:pk>/', views.atualizacliente, name='atualizacliente'),
    path('atualizaordem/<int:pk>/', views.atualizaordem, name='atualizaordem'),
    path('apagarordem/<int:pk>/', views.apagarordem, name='apagarordem'),
    path('apagarcliente/<int:pk>/', views.apagarcliente, name='apagarcliente'),
    path('novaordem/', views.novaordem, name='novaordem')
]