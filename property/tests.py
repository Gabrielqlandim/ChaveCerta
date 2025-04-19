from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from user.models import CustomUser
from property.models import Imovel, ContratoLocacao, Pagamento, Avaliacao

class ImovelTests(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='password123',
            is_active=True  
        )
        self.client.force_authenticate(user=self.user)

    def test_create_imovel(self):
        url = reverse('imovel-list')
        data = {
            "titulo": "Apartamento Teste",
            "descricao": "Descrição do imóvel teste.",
            "endereco": "Rua Teste, 123",
            "tipo": "apartamento",
            "quartos": 2,
            "banheiros": 1,
            "vagas_garagem": 1,
            "valor_aluguel": "1200.00",
            "disponivel": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Imovel.objects.count(), 1)
        self.assertEqual(Imovel.objects.get().titulo, "Apartamento Teste")

    def test_list_imoveis(self):
        Imovel.objects.create(
            proprietario=self.user,
            titulo="Casa Teste",
            descricao="Descrição teste",
            endereco="Rua Teste 456",
            tipo="casa",
            quartos=3,
            banheiros=2,
            vagas_garagem=2,
            valor_aluguel="2000.00",
            disponivel=True
        )
        url = reverse('imovel-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_list_imoveis_disponiveis(self):
        Imovel.objects.create(
            proprietario=self.user,
            titulo="Casa Disponível",
            descricao="Casa disponível para locação",
            endereco="Rua Livre 789",
            tipo="casa",
            quartos=4,
            banheiros=3,
            vagas_garagem=2,
            valor_aluguel="2500.00",
            disponivel=True
        )
        url = reverse('imovel-disponiveis')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_contrato_locacao(self):
        imovel = Imovel.objects.create(
            proprietario=self.user,
            titulo="Casa para Alugar",
            descricao="Casa ampla",
            endereco="Rua do Aluguel 101",
            tipo="casa",
            quartos=3,
            banheiros=2,
            vagas_garagem=1,
            valor_aluguel="1800.00",
            disponivel=True
        )
        url = reverse('contratolocacao-list')
        data = {
            "imovel": imovel.id,
            "data_inicio": "2025-05-01",
            "data_fim": "2026-05-01",
            "valor_mensal": "1800.00",
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_pagamentos_pendentes(self):
        imovel = Imovel.objects.create(
            proprietario=self.user,
            titulo="Casa Pagamento",
            descricao="Pagamento em aberto",
            endereco="Rua Teste 999",
            tipo="casa",
            quartos=2,
            banheiros=1,
            vagas_garagem=1,
            valor_aluguel="1500.00",
            disponivel=True
        )
        contrato = imovel.contratos.create(
            locatario=self.user,
            data_inicio="2025-05-01",
            data_fim="2026-05-01",
            valor_mensal="1500.00"
        )
        Pagamento.objects.create(
            contrato=contrato,
            valor_pago="0.00",
            data_pagamento="2025-05-05",
            confirmado=False
        )
        url = reverse('pagamento-pendentes')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_avaliacao(self):
        imovel = Imovel.objects.create(
            proprietario=self.user,
            titulo="Casa Avaliação",
            descricao="Casa bonita",
            endereco="Rua Beleza 777",
            tipo="casa",
            quartos=2,
            banheiros=2,
            vagas_garagem=1,
            valor_aluguel="1700.00",
            disponivel=True
        )

        contrato = ContratoLocacao.objects.create(
            imovel=imovel,
            locatario=self.user,
            data_inicio="2025-05-01",
            data_fim="2026-05-01",
            valor_mensal="1700.00"
        )
        
        url = reverse('avaliacao-list')
        data = {
            "contrato": contrato.id,
            "nota": 5,
            "comentario": "Ótima casa, bem localizada!"
        }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
