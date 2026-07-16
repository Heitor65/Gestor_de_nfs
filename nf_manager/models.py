from django.db import models
from django.core.exceptions import ValidationError
from brutils import is_valid_cnpj, is_valid_cep, get_address_from_cep,  is_valid_phone, is_valid_email

def _validate_cnpj(value):
    if not is_valid_cnpj(value):
        raise ValidationError("%(value)s não é um CNPJ válido.", params={"value": value})

def _validate_cep(value):
    if value and not is_valid_cep(value):
        raise ValidationError("%(value)s não é um CEP válido.", params={"value": value})

def _validate_phone(value):
    if value and not is_valid_phone(value):
        raise ValidationError("%(value)s não é um telefone válido.", params={"value": value})

def _validate_email(value):
    if value and not is_valid_email(value):
        raise ValidationError("%(value)s não é um email válido.", params={"value": value})


class Nf(models.Model):
    empresa = models.ForeignKey("Empresa", on_delete=models.RESTRICT, related_name="nfs")
    op = models.CharField("Ordem de Produção (OP)", max_length=4, default="")
    cep = models.CharField("CEP", max_length=8, default="", blank=True, null=True, validators=[_validate_cep])
    uf = models.CharField("UF", max_length=2, default="RJ")
    cidade = models.CharField("Cidade", max_length=100, default="")
    bairro = models.CharField("Bairro", max_length=100, default="")
    logradouro = models.CharField("Logradouro", max_length=100, default="")
    numero = models.CharField("Número", max_length=10, default="")
    complemento = models.CharField("Complemento", max_length=100, default="")
    servico = models.CharField("Serviço", max_length=100, default="")
    valor = models.DecimalField("Valor", max_digits=8, decimal_places=2)
    status = models.CharField("Status", max_length=20, choices=[('pendente', 'Pendente'), ('aprovada', 'Aprovada'), ('emitido', 'Emitido'), ('cancelada', 'Cancelada'), ('substituida', 'Substituída')], default='pendente')
    descricao = models.TextField("Descrição (Opcional)", blank=True, null=True)
    numero_nfse = models.CharField("Número da NFSe", max_length=20, blank=True, null=True)
    codigo_verificacao = models.CharField("Código de Verificação", max_length=20, blank=True, null=True)
    data_emissao_nfse = models.DateTimeField("Data de Emissão da NFSe", blank=True, null=True)
    xml_nfse = models.TextField("XML da NFSe", blank=True, null=True)
    mensagens_erro = models.JSONField ("Mensagens de Erro", blank=True, null=True)
    tentativa_emissao_em = models.DateTimeField("Tentativa de Emissão em", blank=True, null=True)
    nota_substituta = models.ForeignKey(
    "self",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="nota_substituida",
    )

    def save(self, *args, **kwargs):
        if self.cep:
            endereco = get_address_from_cep(self.cep, raise_exceptions=True)

            self.uf = endereco["uf"]
            self.cidade = endereco["localidade"]
            self.bairro = endereco["bairro"]
            self.logradouro = endereco["logradouro"]

        super().save(*args, **kwargs)

    def aprovar(self):
        self.status = 'aprovada'
        self.save()
    
    def emitir(self):
        self.status = 'emitido'
        self.save()

    def cancelar(self):
        self.status = 'cancelada'
        self.save()

    def substituir(self):
        self.status = 'substituida'
        self.save()
    
    def __str__(self):
        return f"NF {self.empresa.razao_social} - {self.empresa.cnpj} - {self.op}"

class Empresa(models.Model):
    razao_social = models.CharField("Razão Social", max_length=100, default="")
    cnpj = models.CharField("CNPJ", max_length=14, default="", validators=[_validate_cnpj])
    inscricao_estadual = models.CharField("Inscrição Estadual", max_length=20, default="")
    inscricao_municipal = models.CharField("Inscrição Municipal", max_length=20, default="")

class Contato(models.Model):
    nome = models.CharField("Pessoa de Contato", max_length=100, blank=True, null=True)
    numero_contato = models.CharField("Número de Contato", max_length=20, blank=True, null=True, validators=[_validate_phone])
    email_contato = models.EmailField("Email de Contato", blank=True, null=True, validators=[_validate_email])
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_DEFAULT, default="Sem empresa", related_name="contatos")

class HistoricoAlteracao(models.Model):
    nf = models.ForeignKey(Nf, on_delete=models.DO_NOTHING, related_name="historico_alteracoes")
    data_hora = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField("Usuário", max_length=100, default="")
    campo_alterado = models.CharField("Campo Alterado", max_length=100, default="")
    valor_anterior = models.TextField("Valor Anterior", blank=True, null=True)
    valor_novo = models.TextField("Valor Novo", blank=True, null=True)
    justificativa = models.TextField("Descrição da Alteração", blank=True, null=True)