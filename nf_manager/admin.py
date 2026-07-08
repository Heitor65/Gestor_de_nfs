from django.contrib import admin
from .models import Nf

@admin.action(description='Aprovar NFs selecionadas')
def aprovar_nfs(modeladmin, request, queryset):
    for nf in queryset:
        nf.aprovar()


@admin.register(Nf)
class NfAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('razao_social', 'cnpj', 'op', 'pessoa_contato', 'servico', 'status')
    search_fields = ('razao_social', 'cnpj', 'op', 'pessoa_contato')
    list_editable = ('status',)
    fieldsets = (
        ('Informações da NFSe', {
            'fields': ('razao_social', 'cnpj', 'op', 'codigo_verificacao', 'numero_nfse', 'inscricao_estadual', 'inscricao_municipal')
        }),
        ('Endereço', {
            'fields': ('cep', 'uf', 'cidade', 'bairro', 'logradouro', 'numero', 'complemento')
        }),
        ('Informações de Contato (Opcional)', {
            'fields': ('pessoa_contato', 'numero_contato', 'email_contato')
        }),
        ('Serviço e Status', {
            'fields': ('servico', 'valor', 'status')
        }),
        (None, {
            'fields': ('descricao',)
        }),
    )
    actions = [aprovar_nfs]