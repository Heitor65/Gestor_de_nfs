from django.db import models

class Nf(models.Model):
    razao_social = models.CharField("Razão Social", max_length=100, default="")
    cnpj = models.CharField("CNPJ", max_length=14, default="")
    op = models.CharField("Ordem de Produção (OP)", max_length=4, default="")
    cep = models.CharField("CEP", max_length=8, default="")
    uf = models.CharField("UF", max_length=2, default="RJ")
    cidade = models.CharField("Cidade", max_length=100, default="")
    bairro = models.CharField("Bairro", max_length=100, default="")
    logradouro = models.CharField("Logradouro", max_length=100, default="")
    numero = models.CharField("Número", max_length=10, default="")
    complemento = models.CharField("Complemento", max_length=100, default="")
    inscricao_estadual = models.CharField("Inscrição Estadual", max_length=20, default="")
    inscricao_municipal = models.CharField("Inscrição Municipal", max_length=20, default="")
    pessoa_contato = models.CharField("Pessoa de Contato", max_length=100, blank=True, null=True)
    numero_contato = models.CharField("Número de Contato", max_length=20, blank=True, null=True)
    email_contato = models.EmailField("Email de Contato", blank=True, null=True)
    servico = models.CharField("Serviço", max_length=100, default="")
    valor = models.DecimalField("Valor", max_digits=8, decimal_places=2)
    status = models.CharField("Status", max_length=20, choices=[('pendente', 'Pendente'), ('aprovada', 'Aprovada'), ('rejeitada', 'Rejeitada')], default='pendente')
    descricao = models.TextField("Descrição", blank=True, null=True)

    def __str__(self):
        return f"NF {self.razao_social} - {self.cnpj} - {self.op}"