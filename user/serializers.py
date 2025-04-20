from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from .models import CustomUser

# Serializer para criação de usuário via Djoser 
class CustomUserCreateSerializer(BaseUserCreateSerializer):
    re_password = serializers.CharField(write_only=True, required=True)  # Campo extra

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
        
    def validate(self, attrs):
        password = attrs.get('password')
        re_password = attrs.pop('re_password', None)  

        if password != re_password:
            raise serializers.ValidationError("As senhas não coincidem.")

        return attrs

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este e-mail já está em uso.")
        return value

# Serializer para exibição de usuário
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'telefone',
            'cpf',
            'endereco',
            'imagem_perfil'
        ]
