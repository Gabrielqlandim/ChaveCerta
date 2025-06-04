---

# ChaveCerta - API de Locação de Imóveis

API desenvolvida para gerenciar o cadastro de imóveis para aluguel, permitir a locação e a avaliação dos imóveis.

Este projeto foi criado como parte de um desafio técnico, utilizando Django, Django REST Framework e Djoser para autenticação.

---

## 🚀 Tecnologias Utilizadas

* Python 3.11
* Django 5
* Django REST Framework
* Djoser
* Django Filters
* SimpleJWT (opcional)
* Pillow (para upload de imagens)
* drf-yasg (para documentação Swagger/OpenAPI)

---

## 📋 Funcionalidades

* Cadastro e autenticação de usuários
* Confirmação de e-mail com envio de token
* Alteração de senha
* Cadastro de imóveis para locação
* Locação de imóveis por usuários
* Avaliações dos imóveis locados
* Áreas públicas e restritas, com controle de acesso
* Paginação, busca, filtro e ordenação nas listagens
* Testes automatizados para as principais rotas
* Documentação gerada automaticamente via OpenAPI (Swagger e ReDoc)

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

| Teste                                     | O que valida                        |
| :---------------------------------------- | :---------------------------------- |
| Cadastro de imóvel                        | Criação de imóvel                   |
| Listagem de imóveis                       | Listar todos imóveis                |
| Listagem de imóveis disponíveis           | Listar apenas imóveis disponíveis   |
| Cadastro de contrato de locação           | Criação de contrato para imóvel     |
| Listagem de pagamentos pendentes          | Listar pagamentos em aberto         |
| Cadastro de avaliação                     | Avaliar imóvel locado               |
| Cadastro de usuário com envio de ativação | Criar usuário e enviar e-mail       |
| Ativação de conta de usuário              | Ativar conta com token válido       |
| Atualização do próprio perfil             | Atualizar dados do próprio usuário  |
| Bloqueio de atualização de outro usuário  | Não permitir editar perfil alheio   |
| Login de usuário via token                | Autenticação de usuário com sucesso |

### Validações de Erro

| Teste                                   | O que valida                       |
| :-------------------------------------- | :--------------------------------- |
| Criação de imóvel sem título            | Impede imóvel sem título           |
| Criação de imóvel com aluguel negativo  | Impede imóvel com aluguel negativo |
| Criação de avaliação sem nota           | Impede avaliação sem nota          |
| Criação de contrato sem data de início  | Impede contrato sem data inicial   |
| Criação de pagamento sem valor pago     | Impede pagamento sem valor pago    |
| Cadastro de usuário sem email           | Impede cadastro sem email          |
| Cadastro de usuário com email duplicado | Impede duplicação de email         |
| Ativação de conta com token inválido    | Impede ativação inválida           |
| Login com senha errada                  | Impede autenticação inválida       |
| Atualizar perfil sem estar autenticado  | Bloqueia alteração sem login       |

Para rodar os testes, execute:

```bash
python manage.py test
```

---

## 📄 Documentação

* [Swagger UI](http://localhost:8000/swagger/) — Para visualizar o Swagger, é necessário rodar o servidor Django.
* [ReDoc](http://localhost:8000/redoc/) — Também precisa do servidor rodando.

---

## 🔐 Observação Importante: Ativação de Conta

Ao criar um novo usuário, a API envia um e-mail de ativação com um link no formato:

```
http://127.0.0.1:8000/auth/activate/<uid>/<token>
```

> ⚠️ **Esse link não é clicável (dá erro 404).**

Por padrão, o Djoser gera esse link pensando em aplicações com front-end.
**Como este projeto não possui front-end, a ativação da conta deve ser feita manualmente via POST.**

### Passo a passo para ativar a conta

1. **Após o cadastro**, copie o UID e o TOKEN que estão no link enviado por e-mail.

   Exemplo do link recebido:

   ```
   http://127.0.0.1:8000/auth/activate/Mg/cq9u08-6efc96b0b1d4c66113e53a7b961ef6b5
   ```

   * UID: `Mg`
   * TOKEN: `cq9u08-6efc96b0b1d4c66113e53a7b961ef6b5`

2. **Envie um POST para:**

   ```
   http://127.0.0.1:8000/auth/users/activation/
   ```

   Com o seguinte corpo JSON:

   ```json
   {
     "uid": "Mg",
     "token": "cq9u08-6efc96b0b1d4c66113e53a7b961ef6b5"
   }
   ```

3. **Como fazer isso na prática:**

   * **Usando curl:**

     ```bash
     curl -X POST http://127.0.0.1:8000/auth/users/activation/ \
       -H "Content-Type: application/json" \
       -d '{"uid": "Mg", "token": "cq9u08-6efc96b0b1d4c66113e53a7b961ef6b5"}'
     ```

   * **Ou via Postman/Insomnia:**

     * Método: **POST**
     * URL: `http://127.0.0.1:8000/auth/users/activation/`
     * Body: JSON com os campos `uid` e `token`

4. **Resposta esperada:**

   * **204 No Content** em caso de sucesso (conta ativada!)
   * **400 Bad Request** se o token for inválido ou já tiver sido usado

---

> **Resumo:**
> O link recebido no e-mail serve apenas para te entregar o UID e TOKEN.
> **A ativação real da conta acontece via POST em `/auth/users/activation/`**.

---

**Dica:**
Caso queira testar o fluxo completo de ativação, siga o passo a passo acima após o cadastro de um novo usuário!

---

