from django.contrib import admin
from .models import Nf

@admin.register(Nf)
class NfAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('razao_social', 'cnpj', 'op', 'pessoa_contato', 'servico', 'status')
    search_fields = ('razao_social', 'cnpj', 'op', 'pessoa_contato')
    fieldsets = (
        (None, {
            'fields': ('razao_social', 'cnpj', 'op', 'inscricao_estadual', 'inscricao_municipal')
        }),
        ('Endereço', {
            'fields': ('cep', 'uf', 'cidade', 'bairro', 'logradouro', 'numero', 'complemento')
        }),
        ('Informações de Contato', {
            'fields': ('pessoa_contato', 'numero_contato', 'email_contato')
        }),
        ('Serviço e Status', {
            'fields': ('servico', 'valor', 'status')
        }),
        (None, {
            'fields': ('descricao',)
        }),
    )