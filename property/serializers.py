from rest_framework import serializers
from .models import Imovel, ContratoLocacao, Pagamento, Avaliacao
from user.serializers import CustomUserSerializer

class ImovelSerializer(serializers.ModelSerializer):
    proprietario = CustomUserSerializer(read_only=True)

    class Meta:
        model = Imovel
        fields = '__all__'
    def validate_valor_aluguel(self, value):
        if value < 0:
            raise serializers.ValidationError("O valor do aluguel não pode ser negativo.")
        return value

class ContratoLocacaoSerializer(serializers.ModelSerializer):
    locatario = CustomUserSerializer(read_only=True)
    imovel = serializers.PrimaryKeyRelatedField(queryset=Imovel.objects.all())

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
    contrato = serializers.PrimaryKeyRelatedField(queryset=ContratoLocacao.objects.all())

    class Meta:
        model = Avaliacao
        fields = '__all__'
