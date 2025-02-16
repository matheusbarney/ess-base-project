import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src')))

import pytest
from pytest_bdd import scenario, given, when, then
from fastapi.testclient import TestClient
from src.api.reviews import app
from src.schemas.avaliacao import Avaliacao

@scenario(scenario_name="Se eu não sou dono de uma reserva, não conseguir ocultar comentário deixado na página de uma reserva.", feature_name="../features/reviews.feature")
def test_service_review_nao_dono():
    " Scenario: Se eu não sou dono de uma reserva, não conseguir ocultar comentário deixado na página de uma reserva. "

# Inicializar o cliente de teste
client = TestClient(app)

@pytest.fixture
def context():
    return {}


@given('Sou o usuário "Mike Ehrmantraut" de CPF "4"')
def given_usuario_nao_dono(context):
    context['cpfnj'] = "4"

@given('Dado uma reserva de endereço "08 Negra Arroyo Lane, Albuquerque, PE" que não está no meu nome')
def given_reserva_nao_dono(context):
    context['endereco'] = "308 Negra Arroyo Lane, Albuquerque, PE"

@given('Dado um comentário na reserva de ID "2" que desejo ocultar')
def given_comentario_nao_dono(context):
    context['comentario_id'] = 2

@when('Eu tento ocultar tal comentário')
def when_tentar_ocultar_comentario(context):
    response = client.patch("/avaliacoes/ocultar", params={"cpfnj": context['cpfnj'], "comentario_id": context['comentario_id']})
    context['response'] = response

@then('O comentário não é definido como ocultado')
def then_comentario_nao_ocultado(context):
    response = context['response']
    assert response.status_code == 403
    assert response.json() == {"detail": "Usuário não autorizado a ocultar esta avaliação"}

    # Verificar se o comentário não foi ocultado no banco de dados
    db_ava = client.get("/avaliacoes").json()
    avaliacao = next((a for a in db_ava if a["id"] == context['comentario_id']), None)
    assert avaliacao is not None
    assert avaliacao["oculto"] is False
