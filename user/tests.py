from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from user.models import CustomUser
from django.core import mail
from rest_framework.authtoken.models import Token

class UserTests(APITestCase):

    def test_create_user_and_send_activation_email(self):
        url = '/auth/users/'  
        data = {
            "username": "novouser",
            "email": "novo@example.com",
            "password": "senhaSecreta123456!",
            "re_password": "senhaSecreta123456!",
            "first_name": "Novo",
            "last_name": "Usuario",
            "telefone": "81999999999",
            "cpf": "123.456.789-00",
            "endereco": "Rua dos Testes, 456"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Account activation', mail.outbox[0].subject)

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

        url = '/auth/users/activation/'
        data = {
            'uid': uid,
            'token': token
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        user.refresh_from_db()
        self.assertTrue(user.is_active)

    def test_update_own_profile(self):
        # Cria e autentica o usuário
        user = CustomUser.objects.create_user(
            username="perfilteste",
            email="perfil@example.com",
            password="senha123",
            telefone="00000000000",
            cpf="000.000.000-00",
            endereco="Endereco Antigo"
        )
        self.client.force_authenticate(user=user)

        url = f'/api/user/usuarios/{user.id}/'  # URL para editar o próprio perfil
        data = {
            "telefone": "81988888888",
            "endereco": "Rua Nova Atualizada"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se atualizou
        user.refresh_from_db()
        self.assertEqual(user.telefone, "81988888888")
        self.assertEqual(user.endereco, "Rua Nova Atualizada")

    def test_cannot_update_other_users(self):
        # Cria dois usuários
        user1 = CustomUser.objects.create_user(
            username="user1",
            email="user1@example.com",
            password="senha123"
        )
        user2 = CustomUser.objects.create_user(
            username="user2",
            email="user2@example.com",
            password="senha123",
            cpf="987.654.321-00"
        )
        self.client.force_authenticate(user=user1)

        url = f'/api/user/usuarios/{user2.id}/'  # Tentando editar o perfil de outro usuário
        data = {
            "telefone": "81977777777"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Deve ser proibido!

    def test_login_token(self):
        # Cria usuário
        user = CustomUser.objects.create_user(
            username="loginteste",
            email="loginteste@example.com",
            password="senhaSecreta123"
        )
        url = '/auth/token/login/'
        data = {
            "username": "loginteste",
            "password": "senhaSecreta123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('auth_token', response.data)  # Verifica se recebeu o token
