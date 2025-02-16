from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
import json

def getDB():
    with open(r'C:\Users\mathe\OneDrive\Desktop\College Projects\ess-base-project\backend\src\db\db_reservas.json', 'r') as dbu:
        db = json.load(dbu)
    return db

def saveDB(db):
    with open(r'C:\Users\mathe\OneDrive\Desktop\College Projects\ess-base-project\backend\src\db\db_reservas.json', 'w') as dbu:
        db = json.dump(db, fp=dbu, indent=4)
    return db

class TipoReserva(str, Enum):
    QUARTO = "Quarto"
    CASA = "Casa"
    APARTAMENTO = "Apartamento"
    SALAO = "Salão"

class Reserva(BaseModel):
    ativo: bool = True
    titulo: str
    descricao: str
    imagens: str
    petfriendly: bool
    endereco: str
    tipo: TipoReserva
    disponibilidade: str
    preco: int = 0
    usuario: str
    avalMedia: float = 0
    qntdAlugado: int = 0
    destacado: bool = False