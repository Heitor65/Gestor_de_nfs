from rest_framework import serializers
from .models import Nf, Empresa, Contato

class NfReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nf
        fields = "__all__"
        read_only_fields = [
            "xml_nfse",
            "mensagens_erro",
            "tentativa_emissao_em",
        ]

class NfCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nf
        fields = [
            "empresa",
            "op",
            "cep",
            "uf",
            "cidade",
            "bairro",
            "logradouro",
            "numero",
            "complemento",
            "servico",
            "valor",
            "descricao",
            "numero_nfse",
            "codigo_verificacao",
            "data_emissao_nfse"
        ]

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ContatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contato
        fields = '__all__'