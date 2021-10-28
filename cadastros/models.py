from django.conf import settings
from django.db import models

# Create your models here.
class Cliente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45)
    cnpj = models.CharField(max_length=45)
    endereco = models.CharField(max_length=45, verbose_name='Endereço')
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=4)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=16)
    
class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    usinagem = models.BooleanField()
    montagem = models.BooleanField()
    revisao = models.BooleanField(verbose_name='Revisão')
    motor = models.BooleanField()
    cabecote = models.BooleanField(verbose_name='Cabeçote')
    outros = models.CharField(max_length=20)
    #servico_biela_idbiela INT
    #servico_bloco_idservico_bloco INT
    #servico_comoando_valvula_idservivo_comoando_valvula INT
    #servico_volante_idservico_volante INT
    #servico_motor_idservico_motor INT
