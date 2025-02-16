from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

def getDB():
    with open(os.path.join(os.path.dirname(__file__), '../db/db_usuarios.json'), 'r') as dbu:
        db = json.load(dbu)
    return db

def saveDB(db):
    with open(os.path.join(os.path.dirname(__file__), '../db/db_usuarios.json'), 'w') as dbu:
        json.dump(db, fp=dbu, indent=4)
    return db

class Usuario(BaseModel):
    nome: str
    cpfnj: str
