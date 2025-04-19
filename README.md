# ChaveCerta - API de Locação de Imóveis

API desenvolvida para gerenciar o cadastro de imóveis para aluguel, permitir a locação e a avaliação dos imóveis.

Este projeto foi criado como parte de um desafio técnico, utilizando Django, Django REST Framework e Djoser para autenticação.

---

## 🚀 Tecnologias Utilizadas

- Python 3.11
- Django 5
- Django REST Framework
- Djoser
- Django Filters
- SimpleJWT (opcional)
- Pillow (para upload de imagens)
- drf-yasg (para documentação Swagger/OpenAPI)

---

## 📋 Funcionalidades

- Cadastro e autenticação de usuários
- Confirmação de e-mail com envio de token
- Alteração de senha
- Cadastro de imóveis para locação
- Locação de imóveis por usuários
- Avaliações dos imóveis locados
- Áreas públicas e restritas, com controle de acesso
- Paginação, busca, filtro e ordenação nas listagens
- Testes automatizados para as principais rotas
- Documentação gerada automaticamente via OpenAPI (Swagger e ReDoc)

---

## 🛠️ Como Rodar o Projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/chavecerta.git
cd chavecerta

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Rode as migrações
python manage.py makemigrations
python manage.py migrate

# Rode o servidor
python manage.py runserver
```

---

## 🧪 Testes Automatizados

Foram implementados os seguintes testes:

- Cadastro de imóvel
- Listagem de imóveis
- Cadastro de usuário e envio de e-mail de ativação
- Ativação de conta de usuário


Para rodar os testes, execute:

```bash
python manage.py test
```
---

## 📄 Documentação:

- [Swagger UI](http://localhost:8000/swagger/)
- [ReDoc](http://localhost:8000/redoc/)
