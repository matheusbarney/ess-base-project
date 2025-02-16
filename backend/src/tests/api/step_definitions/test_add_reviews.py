import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src')))

import pytest
from pytest_bdd import scenario, given, when, then
from fastapi.testclient import TestClient
from src.api.reviews import app
from src.schemas.avaliacao import Avaliacao

@scenario(scenario_name="Avaliar reserva durante minha estadia, com um comentário pessoal.", feature_name="../features/reviews.feature")
def test_service_review_reserva():
    " Scenario: Avaliar reserva durante minha estadia, com um comentário pessoal. "

# Inicializar o cliente de teste
client = TestClient(app)

# Variáveis globais para armazenar os dados
avaliacao_data = {}
response = None

@given('Sou o usuário "Heisenberg" de CPF "9"')
def step_impl():
    global usuario_cpfnj
    usuario_cpfnj = "9"

@given('Estou na reserva de endereço "08 Negra Arroyo Lane, Albuquerque, PE"')
def step_impl():
    global reserva_endereco
    reserva_endereco = "08 Negra Arroyo Lane, Albuquerque, PE"

@given('Marco minha "Avaliação" como "5" estrelas e um comentário "Say my name."')
def step_impl():
    global avaliacao_data
    avaliacao_data = {
        "id": 1,
        "usuario": usuario_cpfnj,
        "endereco": reserva_endereco,
        "nota": 5,
        "comentario": "Say my name.",
        "oculto": False
    }

@when('Eu envio a avaliação')
def step_impl():
    global response
    response = client.post("/avaliacoes/add", json=avaliacao_data)

@then('A avaliação é adicionada com sucesso')
def step_impl():
    assert response.status_code == 200
    avaliacao = response.json()
    assert avaliacao["nota"] == 5
    assert avaliacao["comentario"] == "Say my name."
