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
git clone https://github.com/Gabrielqlandim/ChaveCerta
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

Foram implementados 22 testes automatizados, divididos entre fluxos de sucesso e fluxos de erro.

### Fluxos Felizes

| Teste | O que valida |
|:------|:-------------|
| Cadastro de imóvel | Criação de imóvel |
| Listagem de imóveis | Listar todos imóveis |
| Listagem de imóveis disponíveis | Listar apenas imóveis disponíveis |
| Cadastro de contrato de locação | Criação de contrato para imóvel |
| Listagem de pagamentos pendentes | Listar pagamentos em aberto |
| Cadastro de avaliação | Avaliar imóvel locado |
| Cadastro de usuário com envio de ativação | Criar usuário e enviar e-mail |
| Ativação de conta de usuário | Ativar conta com token válido |
| Atualização do próprio perfil | Atualizar dados do próprio usuário |
| Bloqueio de atualização de outro usuário | Não permitir editar perfil alheio |
| Login de usuário via token | Autenticação de usuário com sucesso |

### Validações de Erro

| Teste | O que valida |
|:------|:-------------|
| Criação de imóvel sem título | Impede imóvel sem título |
| Criação de imóvel com aluguel negativo | Impede imóvel com aluguel negativo |
| Criação de avaliação sem nota | Impede avaliação sem nota |
| Criação de contrato sem data de início | Impede contrato sem data inicial |
| Criação de pagamento sem valor pago | Impede pagamento sem valor pago |
| Cadastro de usuário sem email | Impede cadastro sem email |
| Cadastro de usuário com email duplicado | Impede duplicação de email |
| Ativação de conta com token inválido | Impede ativação inválida |
| Login com senha errada | Impede autenticação inválida |
| Atualizar perfil sem estar autenticado | Bloqueia alteração sem login |


Para rodar os testes, execute:

```bash
python manage.py test
```
---

## 📄 Documentação:

- [Swagger UI](http://localhost:8000/swagger/)
- [ReDoc](http://localhost:8000/redoc/)
