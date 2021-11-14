from django.urls import path
from . import views
from .views import IndexView, RegisterView

urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='nome-da-url'),
    path('', IndexView.as_view(), name='home'),
    path('registro/', RegisterView.as_view(), name='registro'),
    path('dashboard/', views.listaordem, name='listaordem'),
    path('cliente/', views.listacliente, name='cliente'),
    path('cadastrocliente/', views.cadastrocliente, name='cadastrocliente'),
    path('atualizacliente/<str:pk>/', views.atualizacliente, name='atualizacliente'),
    path('atualizaordem/<int:pk>/', views.atualizaordem, name='atualizaordem'),
    path('apagarordem/<int:pk>/', views.apagarordem, name='apagarordem'),
    path('apagarcliente/<int:pk>/', views.apagarcliente, name='apagarcliente'),
    path('novaordem/', views.novaordem, name='novaordem')
]