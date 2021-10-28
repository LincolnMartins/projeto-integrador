from django.urls import path
from .views import ClienteCreate

urlpatterns = [
    # path('endereco/', MinhaView.as_view(), name='nome-da-url'),
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),
]
