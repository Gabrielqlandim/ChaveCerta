from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from user.models import CustomUser
from django.core import mail
from rest_framework.authtoken.models import Token
from djoser.utils import encode_uid
from django.contrib.auth.tokens import default_token_generator

class UserTests(APITestCase):

    #testes positivos

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
        user = CustomUser.objects.create_user(
            username="perfilteste",
            email="perfil@example.com",
            password="senha123",
            telefone="00000000000",
            cpf="000.000.000-00",
            endereco="Endereco Antigo"
        )
        self.client.force_authenticate(user=user)

        url = f'/api/user/usuarios/{user.id}/'
        data = {
            "telefone": "81988888888",
            "endereco": "Rua Nova Atualizada"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user.refresh_from_db()
        self.assertEqual(user.telefone, "81988888888")
        self.assertEqual(user.endereco, "Rua Nova Atualizada")

    def test_cannot_update_other_users(self):
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

        url = f'/api/user/usuarios/{user2.id}/'
        data = {
            "telefone": "81977777777"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_login_token(self):
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
        self.assertIn('auth_token', response.data)

    # testes negativos

    def test_create_user_without_username(self):
        url = '/auth/users/'
        data = {
            # "username" faltando
            "email": "semusername@example.com",
            "password": "senha123456!",
            "re_password": "senha123456!",
            "first_name": "Sem",
            "last_name": "Username",
            "telefone": "81999999999",
            "cpf": "123.456.789-10",
            "endereco": "Rua Sem Username"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_without_password(self):
        url = '/auth/users/'
        data = {
            "username": "sempassword",
            "email": "sempassword@example.com",
            "first_name": "Sem",
            "last_name": "Password",
            "telefone": "81999999998",
            "cpf": "987.654.321-00",
            "endereco": "Rua Sem Senha"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_with_existing_username(self):
        CustomUser.objects.create_user(
            username="userduplicado",
            email="user1@example.com",
            password="senha123",
            telefone="00000000001",
            cpf="111.111.111-11"
        )
        url = '/auth/users/'
        data = {
            "username": "userduplicado",  # username duplicado
            "email": "user2@example.com",
            "password": "senhaSecreta123456!",
            "re_password": "senhaSecreta123456!",
            "first_name": "Novo",
            "last_name": "Usuario",
            "telefone": "81999999999",
            "cpf": "222.222.222-22",
            "endereco": "Rua Teste"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_activate_user_with_invalid_token(self):
        user = CustomUser.objects.create_user(
            username="ativarerrado",
            email="ativarerrado@example.com",
            password="senha123",
            is_active=False,
            telefone="00000000002",
            cpf="333.333.333-33"
        )
        uid = encode_uid(user.pk)
        token = "tokeninvalido"

        url = '/auth/users/activation/'
        data = {
            'uid': uid,
            'token': token
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_with_wrong_password(self):
        CustomUser.objects.create_user(
            username="loginerrado",
            email="loginerrado@example.com",
            password="senhaCorreta123",
            telefone="00000000003",
            cpf="444.444.444-44"
        )
        url = '/auth/token/login/'
        data = {
            "username": "loginerrado",
            "password": "senhaErrada456"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_profile_without_authentication(self):
        user = CustomUser.objects.create_user(
            username="semautenticacao",
            email="semautenticacao@example.com",
            password="senha123",
            telefone="00000000004",
            cpf="555.555.555-55"
        )
        url = f'/api/user/usuarios/{user.id}/'
        data = {
            "telefone": "81988888888"
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
