from django.shortcuts import render

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from .models import Imovel, ContratoLocacao, Pagamento, Avaliacao
from .serializers import (
    ImovelSerializer,
    ContratoLocacaoSerializer,
    PagamentoSerializer,
    AvaliacaoSerializer
)

from user.permissions import IsOwnerOrReadOnly, IsLocatarioOrReadOnly, IsEmailVerified

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, IsEmailVerified]

    filterset_fields = ['tipo', 'disponivel', 'quartos']
    search_fields = ['titulo', 'endereco', 'descricao']
    ordering_fields = ['valor_aluguel', 'quartos']

    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        disponiveis = Imovel.objects.filter(disponivel=True)
        serializer = self.get_serializer(disponiveis, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(proprietario=self.request.user)

class ContratoLocacaoViewSet(viewsets.ModelViewSet):
    queryset = ContratoLocacao.objects.all()
    serializer_class = ContratoLocacaoSerializer
    permission_classes = [permissions.IsAuthenticated, IsLocatarioOrReadOnly, IsEmailVerified]

    def perform_create(self, serializer):
        serializer.save(locatario=self.request.user)

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmailVerified]

    @action(detail=False, methods=['get'])
    def pendentes(self, request):
        pendentes = Pagamento.objects.filter(confirmado=False)
        serializer = self.get_serializer(pendentes, many=True)
        return Response(serializer.data)

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [permissions.IsAuthenticated, IsEmailVerified]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
