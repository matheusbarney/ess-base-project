import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src')))

import pytest
from pytest_bdd import scenario, given, when, then
from fastapi.testclient import TestClient
from src.api.reviews import app
from src.schemas.avaliacao import Avaliacao

@scenario(scenario_name="Eu sendo dono de uma reserva, ocultar comentário deixado na página da minha reserva.", feature_name="../features/reviews.feature")
def test_service_review_reserva():
    " Scenario: Eu sendo dono de uma reserva, ocultar comentário deixado na página da minha reserva. "

# Inicializar o cliente de teste
client = TestClient(app)

@pytest.fixture
def context():
    return {}

@given('Sou o usuário "Hank Schrader" de CPF "1"')
def given_usuario(context):
    context['cpfnj'] = "1"

@given('Dado uma reserva no meu nome de endereço "08 Negra Arroyo Lane, Albuquerque, PE"')
def given_reserva(context):
    context['endereco'] = "308 Negra Arroyo Lane, Albuquerque, PE"

@given('Dado um comentário na reserva de ID "1" que desejo ocultar')
def given_comentario(context):
    context['comentario_id'] = 1

@when('Eu coloco para ocultar tal comentário')
def when_ocultar_comentario(context):
    response = client.patch("/avaliacoes/ocultar", params={"cpfnj": context['cpfnj'], "comentario_id": context['comentario_id']})
    context['response'] = response

@then('O comentário é definido como ocultado')
def then_comentario_ocultado(context):
    response = context['response']
    assert response.status_code == 200
    assert response.json() == {"message": "Avaliação marcada como oculta"}

    # Verificar se o comentário foi realmente ocultado no banco de dados
    db_ava = client.get("/avaliacoes").json()
    avaliacao = next((a for a in db_ava if a["id"] == context['comentario_id']), None)
    assert avaliacao is not None
    assert avaliacao["oculto"] is True