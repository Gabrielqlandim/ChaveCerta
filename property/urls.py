from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ImovelViewSet, ContratoLocacaoViewSet, 
    PagamentoViewSet, AvaliacaoViewSet
)

router = DefaultRouter()
router.register(r'imoveis', ImovelViewSet)
router.register(r'contratos', ContratoLocacaoViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
