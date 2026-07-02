from django.db import models
from django.core.exceptions import ValidationError
from brutils import is_valid_cnpj, is_valid_cep, get_address_from_cep,  is_valid_phone, is_valid_email

def validate_cnpj(value):
    if not is_valid_cnpj(value):
        raise ValidationError("%(value)s não é um CNPJ válido.", params={"value": value})

def validate_cep(value):
    if value and not is_valid_cep(value):
        raise ValidationError("%(value)s não é um CEP válido.", params={"value": value})

def validate_phone(value):
    if value and not is_valid_phone(value):
        raise ValidationError("%(value)s não é um telefone válido.", params={"value": value})
    
def validate_email(value):
    if value and not is_valid_email(value):
        raise ValidationError("%(value)s não é um email válido.", params={"value": value})


class Nf(models.Model):
    razao_social = models.CharField("Razão Social", max_length=100, default="")
    cnpj = models.CharField("CNPJ", max_length=14, default="", validators=[validate_cnpj])
    op = models.CharField("Ordem de Produção (OP)", max_length=4, default="")
    cep = models.CharField("CEP", max_length=8, default="", blank=True, null=True, validators=[validate_cep])
    uf = models.CharField("UF", max_length=2, default="RJ")
    cidade = models.CharField("Cidade", max_length=100, default="")
    bairro = models.CharField("Bairro", max_length=100, default="")
    logradouro = models.CharField("Logradouro", max_length=100, default="")
    numero = models.CharField("Número", max_length=10, default="")
    complemento = models.CharField("Complemento", max_length=100, default="")
    inscricao_estadual = models.CharField("Inscrição Estadual", max_length=20, default="")
    inscricao_municipal = models.CharField("Inscrição Municipal", max_length=20, default="")
    pessoa_contato = models.CharField("Pessoa de Contato", max_length=100, blank=True, null=True)
    numero_contato = models.CharField("Número de Contato", max_length=20, blank=True, null=True, validators=[validate_phone])
    email_contato = models.EmailField("Email de Contato", blank=True, null=True, validators=[validate_email])
    servico = models.CharField("Serviço", max_length=100, default="")
    valor = models.DecimalField("Valor", max_digits=8, decimal_places=2)
    status = models.CharField("Status", max_length=20, choices=[('pendente', 'Pendente'), ('aprovada', 'Aprovada'), ('emitido', 'Emitido')], default='pendente')
    descricao = models.TextField("Descrição (Opcional)", blank=True, null=True)

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

    def __str__(self):
        return f"NF {self.razao_social} - {self.cnpj} - {self.op}"