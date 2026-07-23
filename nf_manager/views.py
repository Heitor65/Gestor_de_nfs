from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .services import gerar_planilha_notas_emitidas
from .serializers import NfReadSerializer, NfCreateSerializer, EmpresaSerializer, ContatoSerializer
from .models import Nf, Empresa, Contato

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

class NfViewSet(ModelViewSet):
    queryset = Nf.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return NfReadSerializer
        return NfCreateSerializer

class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ContatoViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer