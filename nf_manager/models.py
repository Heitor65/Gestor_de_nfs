from django.db import models

class Nf(models.Model):
    razao_social = models.CharField(max_length=100, default="")
    cnpj = models.CharField(max_length=14, default="")
    op = models.CharField(max_length=4, default="")
    cep = models.CharField(max_length=8, default="")
    uf = models.CharField(max_length=2, default="RJ")
    cidade = models.CharField(max_length=100, default="")
    bairro = models.CharField(max_length=100, default="")
    logradouro = models.CharField(max_length=100, default="")
    numero = models.CharField(max_length=10, default="")
    complemento = models.CharField(max_length=100, default="")
    inscricao_estadual = models.CharField(max_length=20, default="")
    inscricao_municipal = models.CharField(max_length=20, default="")
    pessoa_contato = models.CharField(max_length=100, blank=True, null=True)
    numero_contato = models.CharField(max_length=20, blank=True, null=True)
    email_contato = models.EmailField(blank=True, null=True)
    servico = models.CharField(max_length=100, default="")
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('aprovada', 'Aprovada'), ('rejeitada', 'Rejeitada')], default='pendente')
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"NF {self.razao_social} - {self.cnpj} - {self.op}"