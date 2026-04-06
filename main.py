from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="NBA Props Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"ok": True, "message": "Backend online"}

@app.get("/audit/recent")
def audit_recent():
    return [
        {
            "jogador": "Luka Doncic",
            "mercado": "AST Over",
            "linha": 8.5,
            "projecao": 10.4,
            "edge": 22.4,
            "consistencia": "5/5",
            "status": "Aprovada",
        },
        {
            "jogador": "Nikola Jokic",
            "mercado": "REB Over",
            "linha": 11.5,
            "projecao": 13.6,
            "edge": 18.3,
            "consistencia": "4/5",
            "status": "Aprovada",
        },
    ]
