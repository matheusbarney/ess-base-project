import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException
from typing import List, Optional
from src.schemas.avaliacao import Avaliacao
from src.schemas.usuario import Usuario
from src.schemas.reserva import Reserva
import json

app = FastAPI()
router = APIRouter()

def getDB():
    with open(os.path.join(os.path.dirname(__file__), '../db/db_avaliacoes.json'), 'r') as dbu:
        db = json.load(dbu)
    return db

def saveDB(db):
    with open(os.path.join(os.path.dirname(__file__), '../db/db_avaliacoes.json'), 'w') as dbu:
        json.dump(db, fp=dbu, indent=4)
    return db

def getUserDB():
    with open(os.path.join(os.path.dirname(__file__), '../db/db_usuarios.json'), 'r') as dbu:
        db = json.load(dbu)
    return db

def getReservaDB():
    with open(os.path.join(os.path.dirname(__file__), '../db/db_reservas.json'), 'r') as dbu:
        db = json.load(dbu)
    return db

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/avaliacoes")
async def get_avaliacoes() -> List[Avaliacao]:
    db_ava = getDB()
    return [Avaliacao(**a) for a in db_ava]

@router.post("/avaliacoes/add")
async def create_avaliacao(avaliacao: Avaliacao):
    db_ava = getDB()
    avaliacao.id = len(db_ava) + 1  # Adiciona um ID único à nova avaliação
    db_ava.append(avaliacao.model_dump())
    saveDB(db_ava)
    return avaliacao

@router.patch("/avaliacoes/ocultar")
async def ocultar_avaliacao(cpfnj: str, comentario_id: int):
    db_ava = getDB()
    db_users = getUserDB()
    db_reservas = getReservaDB()

    # Verificar se o usuário existe
    usuario = next((user for user in db_users if user["cpfnj"] == cpfnj), None)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Encontrar a avaliação correspondente
    avaliacao = next((a for a in db_ava if a["id"] == comentario_id), None)
    if not avaliacao:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    # Encontrar a reserva correspondente ao endereço da avaliação
    reserva = next((r for r in db_reservas if r["endereco"] == avaliacao["endereco"]), None)
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva não encontrada")

    # Verificar se o CPF/CNPJ do usuário que quer ocultar corresponde ao CPF/CNPJ do dono da reserva
    if reserva["usuario"] != cpfnj:
        raise HTTPException(status_code=403, detail="Usuário não autorizado a ocultar esta avaliação")

    # Marcar a avaliação como oculta
    avaliacao["oculto"] = True
    saveDB(db_ava)
    return {"message": "Avaliação marcada como oculta"}

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)