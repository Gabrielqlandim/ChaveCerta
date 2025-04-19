from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import CustomUser

# Serializer para criação de usuário via Djoser (com campos personalizados)
class CustomUserCreateSerializer(BaseUserCreateSerializer):
    telefone = serializers.CharField(required=True)
    cpf = serializers.CharField(required=True)
    endereco = serializers.CharField(required=True)
    imagem_perfil = serializers.ImageField(required=False)

    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = (
            'id',
            'username',
            'email',
            'password',
            're_password',
            'first_name',
            'last_name',
            'telefone',
            'cpf',
            'endereco',
            'imagem_perfil',
        )


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'telefone', 'cpf', 'endereco', 'imagem_perfil']
