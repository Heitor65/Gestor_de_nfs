from django.db import models

class nf(models.Model):
    nome = models.CharField(max_length=100)
    servico = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('aprovada', 'Aprovada'), ('rejeitada', 'Rejeitada')], default='pendente')
    descricao = models.TextField(blanck=True, null=True)