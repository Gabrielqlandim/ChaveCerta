from django.test import TestCase

# Create your tests here.


from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from user.models import CustomUser
from property.models import Imovel

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