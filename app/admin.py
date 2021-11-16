from django.contrib import admin
from .models import Cliente, Ordem
from .forms import Clienteform, Ordemform

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'telefone']
    form = Clienteform
    list_filter = ['nome','cpf']
    search_fields = ['nome', 'cpf']

class OrdemAdmin(admin.ModelAdmin):
    list_display = ['id']
    form = Ordemform
    list_filter = ['id']
    search_fields = ['id']

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Ordem, OrdemAdmin)