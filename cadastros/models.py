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

class ServicoBiela(models.Model):
    medir = models.CharField(max_length=45)
    pesar = models.CharField(max_length=45)
    alinhar = models.CharField(max_length=45)
    bielacol = models.CharField(max_length=45)
    retificar_alojamento_bronzia = models.CharField(max_length=45)
    trocar_bucha = models.CharField(max_length=45)
    retificar_bucha = models.CharField(max_length=45)
    montagem_pistao = models.CharField(max_length=45)

class ServicoVirabrequim(models.Model):
    limpeza = models.CharField(max_length=45)
    teste_trinca_superficial_e_dureza = models.CharField(max_length=45)
    desempenar = models.CharField(max_length=45)
    retificar = models.CharField(max_length=45)
    polir = models.IntegerField()
    balancear = models.CharField(max_length=45)
    tornear_lateral = models.CharField(max_length=45)

class ServicoCabecote(models.Model):
    plaina = models.CharField(max_length=45)
    trocar_guias = models.CharField(max_length=45)
    trocar_sedes_valvulas = models.CharField(max_length=45)
    montagem_valvulas = models.CharField(max_length=45)
    regulagem_valvulas = models.CharField(max_length=45)
    servico_solda = models.CharField(max_length=45)
    teste_hidroestatico = models.CharField(max_length=45)
    banho_quimico = models.CharField(max_length=45)

class ServicoBloco(models.Model):
    limpeza = models.CharField(max_length=45)
    brunir_cilindro = models.CharField(max_length=45)
    retificar_cilindro = models.CharField(max_length=45)
    encamisar_cilindro = models.CharField(max_length=45)
    madrilhar_buchar_comando_valvula = models.CharField(max_length=45)
    mandrilhar_mancais = models.CharField(max_length=45)
    mandrilhar_comando_val_auxiliar = models.CharField(max_length=45)
    plainar = models.CharField(max_length=45)
    adaptar_retentor_polia_carcaca = models.CharField(max_length=45)
    embuchar_mancal_traseiro_carcaca = models.CharField(max_length=45)
    fresar_alojamento_tucho_carcaca = models.CharField(max_length=45)
    virabrequim = models.ForeignKey(ServicoVirabrequim, on_delete=models.PROTECT)
    cabecote = models.ForeignKey(ServicoCabecote, on_delete=models.PROTECT)

class ServicoComandoValvula(models.Model):
    inspecionar = models.CharField(max_length=45)
    desempenar = models.CharField(max_length=45)
    polir = models.CharField(max_length=45)
    retificar = models.CharField(max_length=45)

class ServicoVolante(models.Model):
    retificar = models.CharField(max_length=45)
    balancear = models.CharField(max_length=45)

class ServicoMotor(models.Model):
    desmontagem = models.CharField(max_length=45)
    limpezaCompleta = models.BooleanField()
    limpezaParcial = models.BooleanField()
    montagemCompleta = models.BooleanField()
    montagem_Parcial = models.BooleanField()
    pintura = models.CharField(max_length=45)
    remocao = models.CharField(max_length=45)
    instalacao = models.CharField(max_length=45)
    servico_motorcol = models.CharField(max_length=45)

class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    usinagem = models.BooleanField()
    montagem = models.BooleanField()
    revisao = models.BooleanField(verbose_name='Revisão')
    motorCompleto = models.BooleanField()
    cabecote = models.BooleanField(verbose_name='Cabeçote')
    outros = models.CharField(max_length=20)
    biela = models.ForeignKey(ServicoBiela, on_delete=models.PROTECT)
    bloco = models.ForeignKey(ServicoBloco, on_delete=models.PROTECT)
    comandoValvula = models.ForeignKey(ServicoComandoValvula, on_delete=models.PROTECT)
    volante = models.ForeignKey(ServicoVolante, on_delete=models.PROTECT)
    motor = models.ForeignKey(ServicoMotor, on_delete=models.PROTECT)

class Pecas(models.Model):
    item = models.CharField(max_length=45)
    cod_fabricante = models.CharField(max_length=45)
    qtde_atual = models.IntegerField()
    qtde_minima = models.IntegerField()
    ultima_compra = models.DateField()
    descricao = models.CharField(max_length=45)
