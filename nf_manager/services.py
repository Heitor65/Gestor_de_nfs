from openpyxl import Workbook
from nf_manager.models import Nf

def gerar_planilha_notas_emitidas(mes, ano):
    notas = Nf.objects.filter(
        data_emissao_nfse__year=ano,
        data_emissao_nfse__month=mes,
        status='emitido',
    )

    wb = Workbook()
    sheet = wb.active
    sheet.title = "Notas Emitidas"
    sheet['b6'] = "data"
    sheet['c6'] = "empresa"
    sheet['d6'] = "op"
    sheet['e6'] = "valor"
    sheet['f6'] = "numero_nfse"

    for i, nota in enumerate(notas, start=7):
        sheet[f'b{i}'] = nota.data_emissao_nfse
        sheet[f'c{i}'] = nota.empresa.razao_social
        sheet[f'd{i}'] = nota.op
        sheet[f'e{i}'] = nota.valor
        sheet[f'f{i}'] = nota.numero_nfse

    return wb