from os import truncate
from django.conf import settings
from django.db import models

# Create your models here.
class Cliente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=18, blank=True, null=True, unique=True)
    cnpj = models.CharField(max_length=18, blank=True, null=True, unique=True)
    email = models.EmailField(blank=True, null=True)
    endereco = models.CharField(max_length=45, verbose_name='Endereço')
    bairro = models.CharField(max_length=45)
    cidade = models.CharField(max_length=45)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    telefone = models.CharField(max_length=16)

    def __str__(self):
        return "{}".format(self.nome)

class Ordem(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_entrada = models.DateField()
    data_saida = models.DateField(blank=True, null=True)
    numero_chassi = models.CharField(max_length=25, blank=True, null=True)
    numero_bloco = models.CharField(max_length=25, blank=True, null=True)
    modelo_motor = models.CharField(max_length=50, blank=True, null=True)
    pistao_com_anel = models.BooleanField(default=False)
    quant_pist_c_anel = models.IntegerField(blank=True, null=True)
    desc_pist_c_anel = models.CharField(max_length=15, blank=True, null=True)
    aneis_do_pistao = models.BooleanField(default=False)
    quant_aneis_do_pistao = models.IntegerField(blank=True, null=True)
    desc_aneis_do_pistao = models.CharField(max_length=15, blank=True, null=True)
    retentor_tras = models.BooleanField(default=False)
    quant_retentor_tras = models.IntegerField(blank=True, null=True)
    desc_retentor_tras = models.CharField(max_length=15, blank=True, null=True)
    kits_motor = models.BooleanField(default=False)
    quant_kits_motor = models.IntegerField(blank=True, null=True)
    desc_quant_kits_motor = models.CharField(max_length=15, blank=True, null=True)
    bronz_biela = models.BooleanField(default=False)
    quant_bronz_biela = models.IntegerField(blank=True, null=True)
    desc_bronz_biela = models.CharField(max_length=15, blank=True, null=True)
    bronzina_mancal = models.BooleanField(default=False)
    quant_bronzina_mancal = models.IntegerField(blank=True, null=True)
    desc_bronzina_mancal = models.CharField(max_length=15, blank=True, null=True)
    bucha_comando = models.BooleanField(default=False)
    quant_bucha_comando = models.IntegerField(blank=True, null=True)
    desc_bucha_comando = models.CharField(max_length=15, blank=True, null=True)
    bucha_biela = models.BooleanField(default=False)
    quant_bucha_biela = models.IntegerField(blank=True, null=True)
    desc_bucha_biela = models.CharField(max_length=15, blank=True, null=True)
    paraf_biela = models.BooleanField(default=False)
    quant_paraf_biela = models.IntegerField(blank=True, null=True)
    desc_paraf_biela = models.CharField(max_length=15, blank=True, null=True)
    meia_lua = models.BooleanField(default=False)
    quant_meia_lua = models.IntegerField(blank=True, null=True)
    desc_meia_lua = models.CharField(max_length=15, blank=True, null=True)
    jogo_de_juntas = models.BooleanField(default=False)
    quant_jogo_de_juntas = models.IntegerField(blank=True, null=True)
    desc_jogo_de_juntas = models.CharField(max_length=15, blank=True, null=True)
    retentor_diant = models.BooleanField(default=False)
    quant_retentor_diant = models.IntegerField(blank=True, null=True)
    desc_retentor_diant = models.CharField(max_length=15, blank=True, null=True)
    retentor_tras = models.BooleanField(default=False)
    quant_retentor_tras = models.IntegerField(blank=True, null=True)
    desc_quant_retentor_tras = models.CharField(max_length=15, blank=True, null=True)
    sedes_escape = models.BooleanField(default=False)
    quant_sedes_escape = models.IntegerField(blank=True, null=True)
    desc_sedes_escape = models.CharField(max_length=15, blank=True, null=True)
    sedes_admissao = models.BooleanField(default=False)
    quant_sedes_admissao = models.IntegerField(blank=True, null=True)
    desc_sedes_admissao = models.CharField(max_length=15, blank=True, null=True)
    guias_escape = models.BooleanField(default=False)
    quant_guias_escape = models.IntegerField(blank=True, null=True)
    desc_guias_escape = models.CharField(max_length=15, blank=True, null=True)
    guias_admissao = models.BooleanField(default=False)
    quant_guias_admissao = models.IntegerField(blank=True, null=True)
    desc_guias_admissao = models.CharField(max_length=15, blank=True, null=True)
    valvulas_escape = models.BooleanField(default=False)
    quant_valvulas_escape = models.IntegerField(blank=True, null=True)
    desc_valvulas_escape = models.CharField(max_length=15, blank=True, null=True)
    valvulas_admissao = models.BooleanField(default=False)
    quant_valvulas_admissao = models.IntegerField(blank=True, null=True)
    desc_valvulas_admissao = models.CharField(max_length=15, blank=True, null=True)
    chavetas = models.BooleanField(default=False)
    quant_chavetas = models.IntegerField(blank=True, null=True)
    desc_chavetas = models.CharField(max_length=15, blank=True, null=True)
    molas = models.BooleanField(default=False)
    quant_molas = models.IntegerField(blank=True, null=True)
    desc_molas = models.CharField(max_length=15, blank=True, null=True)
    pratos = models.BooleanField(default=False)
    quant_pratos = models.IntegerField(blank=True, null=True)
    desc_pratos = models.CharField(max_length=15, blank=True, null=True)
    calcos = models.BooleanField(default=False)
    quant_calcos = models.IntegerField(blank=True, null=True)
    desc_calcos = models.CharField(max_length=15, blank=True, null=True)
    vedadores = models.BooleanField(default=False)
    quant_vedadores = models.IntegerField(blank=True, null=True)
    desc_vedadores = models.CharField(max_length=15, blank=True, null=True)
    tucho_valvulas = models.BooleanField(default=False)
    quant_tucho_valvulas = models.IntegerField(blank=True, null=True)
    desc_tucho_valvulas = models.CharField(max_length=15, blank=True, null=True)
    vareta_valvulas = models.BooleanField(default=False)
    quant_vareta_valvulas = models.IntegerField(blank=True, null=True)
    desc_vareta_valvulas = models.CharField(max_length=15, blank=True, null=True)
    porca_reguladora = models.BooleanField(default=False)
    quant_porca_reguladora = models.IntegerField(blank=True, null=True)
    desc_porca_reguladora = models.CharField(max_length=15, blank=True, null=True)
    regl_balanceiro = models.BooleanField(default=False)
    quant_regl_balanceiro = models.IntegerField(blank=True, null=True)
    desc_regl_balanceiro = models.CharField(max_length=15, blank=True, null=True)
    comando_valvula = models.BooleanField(default=False)
    quant_comando_valvula = models.IntegerField(blank=True, null=True)
    desc_comando_valvula = models.CharField(max_length=15, blank=True, null=True)
    engr_comando = models.BooleanField(default=False)
    quant_engr_comando = models.IntegerField(blank=True, null=True)
    desc_engr_comando = models.CharField(max_length=15, blank=True, null=True)
    flange_comando = models.BooleanField(default=False)
    quant_flange_comando = models.IntegerField(blank=True, null=True)
    desc_flange_comando = models.CharField(max_length=15, blank=True, null=True)
    chaveta_comando = models.BooleanField(default=False)
    quant_chaveta_comando = models.IntegerField(blank=True, null=True)
    desc_chaveta_comando = models.CharField(max_length=15, blank=True, null=True)
    eixo_balanceiro = models.BooleanField(default=False)
    quant_eixo_balanceiro = models.IntegerField(blank=True, null=True)
    desc_eixo_balanceiro = models.CharField(max_length=15, blank=True, null=True)
    bucha_balanceiro = models.BooleanField(default=False)
    quant_bucha_balanceiro = models.IntegerField(blank=True, null=True)
    desc_bucha_balanceiro = models.CharField(max_length=15, blank=True, null=True)
    balanceiro = models.BooleanField(default=False)
    quant_balanceiro = models.IntegerField(blank=True, null=True)
    desc_balanceiro = models.CharField(max_length=15, blank=True, null=True)
    suporte_balanceiro = models.BooleanField(default=False)
    quant_suporte_balanceiro = models.IntegerField(blank=True, null=True)
    desc_suporte_balanceiro = models.CharField(max_length=15, blank=True, null=True)
    paraf_balanceiro = models.BooleanField(default=False)
    quant_paraf_balanceiro = models.IntegerField(blank=True, null=True)
    desc_paraf_balanceiro = models.CharField(max_length=15, blank=True, null=True)
    trava_balanceiro = models.BooleanField(default=False)
    quant_trava_balanceiro = models.IntegerField(blank=True, null=True)
    desc_trava_balanceiro = models.CharField(max_length=15, blank=True, null=True)
    valvula_pressao = models.BooleanField(default=False)
    quant_valvula_pressao = models.IntegerField(blank=True, null=True)
    desc_valvula_pressao = models.CharField(max_length=15, blank=True, null=True)
    peneira = models.BooleanField(default=False)
    quant_peneira = models.IntegerField(blank=True, null=True)
    desc_peneira = models.CharField(max_length=15, blank=True, null=True)
    bomba_oleo = models.BooleanField(default=False)
    quant_bomba_oleo = models.IntegerField(blank=True, null=True)
    desc_bomba_oleo = models.CharField(max_length=15, blank=True, null=True)
    bomba_agua = models.BooleanField(default=False)
    quant_bomba_agua = models.IntegerField(blank=True, null=True)
    desc_bomba_agua = models.CharField(max_length=15, blank=True, null=True)
    suporte_bba_agua = models.BooleanField(default=False)
    quant_suporte_bba_agua = models.IntegerField(blank=True, null=True)
    desc_suporte_bba_agua = models.CharField(max_length=15, blank=True, null=True)
    valv_termostatica = models.BooleanField(default=False)
    quant_valv_termostatica = models.IntegerField(blank=True, null=True)
    desc_valv_termostatica = models.CharField(max_length=15, blank=True, null=True)
    bocal_agua = models.BooleanField(default=False)
    quant_bocal_agua = models.IntegerField(blank=True, null=True)
    desc_bocal_agua = models.CharField(max_length=15, blank=True, null=True)
    cx_valv_termost = models.BooleanField(default=False)
    quant_cx_valv_termost = models.IntegerField(blank=True, null=True)
    desc_cx_valv_termost = models.CharField(max_length=15, blank=True, null=True)
    mang_valv_termost = models.BooleanField(default=False)
    quant_mang_valv_termost = models.IntegerField(blank=True, null=True)
    desc_mang_valv_termost = models.CharField(max_length=15, blank=True, null=True)
    arruelas_mancal = models.BooleanField(default=False)
    quant_arruelas_mancal = models.IntegerField(blank=True, null=True)
    desc_arruelas_mancal = models.CharField(max_length=15, blank=True, null=True)
    mang_bba_agua = models.BooleanField(default=False)
    quant_mang_bba_agua = models.IntegerField(blank=True, null=True)
    desc_mang_bba_agua = models.CharField(max_length=15, blank=True, null=True)
    cremalheira = models.BooleanField(default=False)
    quant_cremalheira = models.IntegerField(blank=True, null=True)
    desc_cremalheira = models.CharField(max_length=15, blank=True, null=True)
    paraf_volante = models.BooleanField(default=False)
    quant_paraf_volante = models.IntegerField(blank=True, null=True)
    desc_paraf_volante = models.CharField(max_length=15, blank=True, null=True)
    paraf_cabecote = models.BooleanField(default=False)
    quant_paraf_cabecote = models.IntegerField(blank=True, null=True)
    desc_paraf_cabecote = models.CharField(max_length=15, blank=True, null=True)
    colar_engrenagem = models.BooleanField(default=False)
    quant_colar_engrenagem = models.IntegerField(blank=True, null=True)
    desc_colar_engrenagem = models.CharField(max_length=15, blank=True, null=True)
    chaveta_virarbequim = models.BooleanField(default=False)
    quant_chaveta_virarbequim = models.IntegerField(blank=True, null=True)
    desc_chaveta_virarbequim = models.CharField(max_length=15, blank=True, null=True)
    vareta_oleo = models.BooleanField(default=False)
    quant_vareta_oleo = models.IntegerField(blank=True, null=True)
    desc_vareta_oleo = models.CharField(max_length=15, blank=True, null=True)
    engr_virabrequim = models.BooleanField(default=False)
    quant_engr_virabrequim = models.IntegerField(blank=True, null=True)
    desc_engr_virabrequim = models.CharField(max_length=15, blank=True, null=True)
    pistao_compressor = models.BooleanField(default=False)
    quant_pistao_compressorv = models.IntegerField(blank=True, null=True)
    desc_pistao_compressor = models.CharField(max_length=15, blank=True, null=True)
    aneis_compressor = models.BooleanField(default=False)
    quant_aneis_compressor = models.IntegerField(blank=True, null=True)
    desc_aneis_compressor = models.CharField(max_length=15, blank=True, null=True)
    bronz_biela_compr = models.BooleanField(default=False)
    quant_bronz_biela_compr = models.IntegerField(blank=True, null=True)
    desc_bronz_biela_compr = models.CharField(max_length=15, blank=True, null=True)
    bucha_biela_compr = models.BooleanField(default=False)
    quant_bucha_biela_compr = models.IntegerField(blank=True, null=True)
    desc_bucha_biela_compr = models.CharField(max_length=15, blank=True, null=True)
    reparo_compressor = models.BooleanField(default=False)
    quant_reparo_compressor = models.IntegerField(blank=True, null=True)
    desc_reparo_compressor = models.CharField(max_length=15, blank=True, null=True)
    bucha_mancal_compr = models.BooleanField(default=False)
    quant_bucha_mancal_compr = models.IntegerField(blank=True, null=True)
    desc_bucha_mancal_compr = models.CharField(max_length=15, blank=True, null=True)
    mangueira = models.BooleanField(default=False)
    quant_mangueira = models.IntegerField(blank=True, null=True)
    desc_mangueira = models.CharField(max_length=15, blank=True, null=True)
    camisa_cilindro = models.BooleanField(default=False)
    quant_camisa_cilindro = models.IntegerField(blank=True, null=True)
    desc_camisa_cilindro = models.CharField(max_length=15, blank=True, null=True)
    abracadeira = models.BooleanField(default=False)
    quant_abracadeira = models.IntegerField(blank=True, null=True)
    desc_abracadeira = models.CharField(max_length=15, blank=True, null=True)
    rep_compressor_sup = models.BooleanField(default=False)
    quant_rep_compressor_sup = models.IntegerField(blank=True, null=True)
    desc_rep_compressor_sup = models.CharField(max_length=15, blank=True, null=True)
    rep_compressor_inf = models.BooleanField(default=False)
    quant_rep_compressor_inf = models.IntegerField(blank=True, null=True)
    desc_rep_compressor_inf = models.CharField(max_length=15, blank=True, null=True)
    filtro_lubrificante = models.BooleanField(default=False)
    quant_filtro_lubrificante = models.IntegerField(blank=True, null=True)
    desc_filtro_lubrificante = models.CharField(max_length=15, blank=True, null=True)
    valv_filtro_lubrif = models.BooleanField(default=False)
    quant_valv_filtro_lubrif = models.IntegerField(blank=True, null=True)
    desc_valv_filtro_lubrif = models.CharField(max_length=15, blank=True, null=True)
    outras_peca = models.TextField(max_length=1000, blank=True, null=True)
    componetes = models.CharField(max_length=50, blank=True, null=True)
    turbina = models.BooleanField(default=False)
    c_carter = models.BooleanField(default=False)
    c_bujao = models.BooleanField(default=False)
    c_capas = models.BooleanField(default=False)
    c_parafuros = models.BooleanField(default=False)
    quant_parafuros = models.IntegerField(blank=True, null=True)
    bulbo_temp = models.BooleanField(default=False)
    alternador = models.BooleanField(default=False)
    arranque_montado = models.BooleanField(default=False)
    c_peneira = models.BooleanField(default=False)
    bomba_hidraulica = models.BooleanField(default=False)
    c_flexivel = models.BooleanField(default=False)
    polia = models.BooleanField(default=False)
    tubo_admissao = models.BooleanField(default=False)
    tubo_escape = models.BooleanField(default=False)
    carcaca = models.BooleanField(default=False)
    volante = models.BooleanField(default=False)
    plato = models.BooleanField(default=False)
    friccao = models.BooleanField(default=False)
    paraf_carter = models.BooleanField(default=False)
    quant_paraf_carter = models.IntegerField(blank=True, null=True)
    tampa_distribuicao = models.BooleanField(default=False)
    tampa_valvulas = models.BooleanField(default=False)
    tampa_lateral = models.BooleanField(default=False)
    bielas = models.BooleanField(default=False)
    c_pistao = models.BooleanField(default=False)
    comando = models.BooleanField(default=False)
    c_polia = models.BooleanField(default=False)
    suporte_motor = models.BooleanField(default=False)
    cano_vareta = models.BooleanField(default=False)
    filtro_comb = models.BooleanField(default=False)
    acelerador = models.BooleanField(default=False)