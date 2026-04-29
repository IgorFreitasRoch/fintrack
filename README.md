# FinTrack 💰

Aplicação pessoal de controle financeiro desenvolvida como projeto de aprendizado
em desenvolvimento full stack. O objetivo é organizar receitas, despesas e 
acompanhar o saldo de forma simples e segura.

---

## Tecnologias

**Backend**
- Python 3.x
- FastAPI
- SQLAlchemy (ORM)
- Pydantic (validação)
- bcrypt (criptografia de senhas)
- JWT (autenticação)

**Frontend**
- HTML5 semântico
- CSS3 (framework próprio)
- JavaScript (Vanilla)

**Banco de dados**
- SQLite (desenvolvimento local)
- PostgreSQL (produção)

**Documentação**
- Swagger UI — disponível em `/docs` ao rodar o backend

---

## Funcionalidades implementadas

- [ ] Autenticação de usuários (registro e login)
- [ ] Criptografia de senhas com bcrypt
- [ ] Autorização via JWT
- [ ] Cadastro de despesas e receitas
- [ ] Despesas recorrentes com cron job
- [ ] Dashboard com saldo atual
- [ ] Documentação automática da API

---

## Como rodar localmente

### Pré-requisitos
- Python 3.10+
- Node.js (para ferramentas de frontend)

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
Abra o arquivo `frontend/index.html` diretamente no navegador.

---

## Variáveis de ambiente

Copie o arquivo `.env.example`, renomeie para `.env` e preencha:

```bash
cp .env.example .env
```

---

## Documentação da API

Com o backend rodando, acesse:
http://localhost:8000/docs

---

## Autor

Feito com curiosidade por Igor.