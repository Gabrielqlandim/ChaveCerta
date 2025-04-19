from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from user.models import CustomUser
from django.core import mail

class UserTests(APITestCase):
    def test_create_user_and_send_activation_email(self):
        
        url = reverse('user-list')  
        data = {
            "username": "novouser",
            "email": "novo@example.com",
            "password": "senha123",
            "first_name": "Novo",
            "last_name": "Usuario",
            "telefone": "81999999999",
            "cpf": "123.456.789-00",
            "endereco": "Rua dos Testes, 456"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Ative sua conta', mail.outbox[0].subject)

    def test_activate_user_account(self):
        
        user = CustomUser.objects.create_user(
            username="ativarteste",
            email="ativar@example.com",
            password="senha123",
            is_active=False  
        )

        
        from djoser.utils import encode_uid
        from django.contrib.auth.tokens import default_token_generator

        uid = encode_uid(user.pk)
        token = default_token_generator.make_token(user)

        
        url = reverse('user-activation')  
        data = {
            'uid': uid,
            'token': token
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        
        user.refresh_from_db()
        self.assertTrue(user.is_active)
