from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Imovel, ContratoLocacao, Pagamento, Avaliacao
from .serializers import (
    ImovelSerializer,
    ContratoLocacaoSerializer,
    PagamentoSerializer,
    AvaliacaoSerializer
)

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(proprietario=self.request.user)

class ContratoLocacaoViewSet(viewsets.ModelViewSet):
    queryset = ContratoLocacao.objects.all()
    serializer_class = ContratoLocacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(locatario=self.request.user)

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer
    permission_classes = [permissions.IsAuthenticated]

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
