from django.contrib import admin
from django.urls import path
from .models import Nf, Empresa, Contato
from .views import exportar_notas_mes


@admin.action(description='Aprovar NFs selecionadas')
def aprovar_nfs(modeladmin, request, queryset):
    for nf in queryset:
        nf.aprovar()


@admin.register(Nf)
class NfAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('op', 'empresa__razao_social', 'servico', 'status')
    search_fields = ('op', 'empresa__razao_social', 'empresa__cnpj')
    list_editable = ('status',)
    fieldsets = (
        ('Informações da NFSe', {
            'fields': ('empresa', 'op', 'codigo_verificacao', 'numero_nfse')
        }),
        ('Endereço', {
            'fields': ('cep', 'uf', 'cidade', 'bairro', 'logradouro', 'numero', 'complemento')
        }),
        ('Serviço e Status', {
            'fields': ('servico', 'valor', 'status')
        }),
        (None, {
            'fields': ('descricao',)
        }),
    )
    actions = [aprovar_nfs]

    def get_urls(self):
        urls_originais = super().get_urls()
        urls_novas = [
            path('exportar/', self.admin_site.admin_view(exportar_notas_mes), name='nf_exportar'),
        ]
        return urls_novas + urls_originais


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'cnpj')
    search_fields = ('razao_social', 'cnpj', 'inscricao_estadual', 'inscricao_municipal')

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'numero_contato', 'email_contato', 'empresa')
    search_fields = ('nome', 'numero_contato', 'email_contato', 'empresa__razao_social')