from django.shortcuts import render
from django.http import HttpResponse
from .services import gerar_planilha_notas_emitidas

def exportar_notas_mes(request):
    mes = int(request.GET.get('mes'))
    ano = int(request.GET.get('ano'))

    wb = gerar_planilha_notas_emitidas(mes, ano)

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response['Content-Disposition'] = f'attachment; filename="notas_emitidas_{mes:02d}_{ano}.xlsx"'
    wb.save(response)

    return response