from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from user.models import CustomUser
from property.models import Imovel, ContratoLocacao, Pagamento, Avaliacao

class ImovelTests(APITestCase):

    #testes positivos
    
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
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    #testes negativos 

    def test_create_imovel_without_title(self):
        url = reverse('imovel-list')
        data = {
            # "titulo" faltando
            "descricao": "Descrição teste sem título",
            "endereco": "Rua Teste",
            "tipo": "apartamento",
            "quartos": 2,
            "banheiros": 1,
            "vagas_garagem": 1,
            "valor_aluguel": "1500.00",
            "disponivel": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_imovel_with_negative_price(self):
        url = reverse('imovel-list')
        data = {
            "titulo": "Apartamento Bugado",
            "descricao": "Valor negativo",
            "endereco": "Rua Zero",
            "tipo": "apartamento",
            "quartos": 1,
            "banheiros": 1,
            "vagas_garagem": 0,
            "valor_aluguel": "-500.00",  # valor negativo
            "disponivel": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_avaliacao_without_nota(self):
        imovel = Imovel.objects.create(
            proprietario=self.user,
            titulo="Casa Avaliação Erro",
            descricao="Sem nota",
            endereco="Rua Erro",
            tipo="casa",
            quartos=2,
            banheiros=1,
            vagas_garagem=1,
            valor_aluguel="1000.00",
            disponivel=True
        )
        contrato = ContratoLocacao.objects.create(
            imovel=imovel,
            locatario=self.user,
            data_inicio="2025-01-01",
            data_fim="2025-12-31",
            valor_mensal="1000.00"
        )
        url = reverse('avaliacao-list')
        data = {
            "contrato": contrato.id,
            # "nota" faltando
            "comentario": "Sem nota aqui!"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_contrato_without_data_inicio(self):
        imovel = Imovel.objects.create(
            proprietario=self.user,
            titulo="Imóvel para contrato",
            descricao="Teste contrato sem data início",
            endereco="Rua do Contrato",
            tipo="casa",
            quartos=3,
            banheiros=2,
            vagas_garagem=1,
            valor_aluguel="2000.00",
            disponivel=True
        )
        url = reverse('contratolocacao-list')
        data = {
            "imovel": imovel.id,
            "data_fim": "2026-05-01",
            "valor_mensal": "2000.00",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_pagamento_without_valor_pago(self):
        imovel = Imovel.objects.create(
            proprietario=self.user,
            titulo="Imóvel Pagamento Teste",
            descricao="Teste sem valor_pago",
            endereco="Rua Sem Valor",
            tipo="casa",
            quartos=2,
            banheiros=1,
            vagas_garagem=1,
            valor_aluguel="1500.00",
            disponivel=True
        )
        contrato = ContratoLocacao.objects.create(
            imovel=imovel,
            locatario=self.user,
            data_inicio="2025-05-01",
            data_fim="2026-05-01",
            valor_mensal="1500.00"
        )
        url = reverse('pagamento-list')
        data = {
            "contrato": contrato.id,
            "data_pagamento": "2025-06-05",
            "confirmado": False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
