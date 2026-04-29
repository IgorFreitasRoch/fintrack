from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FinTrack API",
    description="API de controle financeiro pessoal",
    version="0.1.0"
)

# Permite o frontend se comunicar com o backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "FinTrack API online"}

@app.get("/despesas")
def listar_despesas():
    # Dados mockados por enquanto — vamos substituir pelo banco depois
    return [
        {"id": 1, "categoria": "Alimentação", "valor": 150.00, "data": "2026-04-01"},
        {"id": 2, "categoria": "Transporte", "valor": 80.50,  "data": "2026-04-03"},
        {"id": 3, "categoria": "Lazer",       "valor": 200.00, "data": "2026-04-10"},
    ]