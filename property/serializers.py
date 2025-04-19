from rest_framework import serializers
from .models import Imovel, ContratoLocacao, Pagamento, Avaliacao
from user.serializers import CustomUserSerializer

class ImovelSerializer(serializers.ModelSerializer):
    proprietario = CustomUserSerializer(read_only=True)

    class Meta:
        model = Imovel
        fields = '__all__'

class ContratoLocacaoSerializer(serializers.ModelSerializer):
    locatario = CustomUserSerializer(read_only=True)
    imovel = ImovelSerializer(read_only=True)

    class Meta:
        model = ContratoLocacao
        fields = '__all__'

class PagamentoSerializer(serializers.ModelSerializer):
    contrato = ContratoLocacaoSerializer(read_only=True)

    class Meta:
        model = Pagamento
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    usuario = CustomUserSerializer(read_only=True)
    contrato = ContratoLocacaoSerializer(read_only=True)

    class Meta:
        model = Avaliacao
        fields = '__all__'
