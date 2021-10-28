from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Cliente

# Create your views here.
class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'cpf', 'cnpj', 'endereco', 'bairro', 'cidade', 'estado', 'cep', 'telefone']
    template_name = 'cadastros/form.html'
    sucess_url = reverse_lazy('home')