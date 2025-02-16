import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src')))

import pytest
from pytest_bdd import scenario, given, when, then, parsers
from fastapi.testclient import TestClient
from src.api.reviews import app
from src.service.impl.review_service import ReviewService

@scenario(scenario_name="Avaliar reserva durante minha estadia, com um comentário pessoal.", feature_name="../features/reviews.feature")
def test_service_review_reserva():
    " Scenario: Avaliar reserva durante minha estadia, com um comentário pessoal. "

# @scenario(scenario_name="Eu sendo dono de uma reserva, ocultar comentário deixado na página da minha reserva.", feature_name="../features/reviews.feature")
# def test_service_hide_review():
#     " Scenario: Eu sendo dono de uma reserva, ocultar comentário deixado na página da minha reserva. "

# Inicializar o cliente de teste
client = TestClient(app)

@pytest.fixture
def context():
    return {}

@given(parsers.cfparse('Sou o usuário "{usuario}" de CPF "{cpf}"'))
def given_usuario(context, usuario: str, cpf: str):
    context['cpfnj'] = cpf

@given(parsers.cfparse('Estou na reserva de endereço "{endereco}"'))
def given_reserva(context, endereco: str):
    context['endereco'] = endereco

@given(parsers.cfparse('Marco minha "Avaliação" como "{nota:d}" estrelas e um comentário "{comentario}"'))
def given_avaliacao(context, nota: int, comentario: str):
    context['avaliacao_data'] = {
        "id": 1,
        "usuario": context['cpfnj'],
        "endereco": context['endereco'],
        "nota": nota,
        "comentario": comentario,
        "oculto": False
    }

@when('Eu envio a avaliação')
def when_envio_avaliacao(context):
    context['response'] = ReviewService.add_review(context['avaliacao_data'])

@then('A avaliação é adicionada com sucesso')
def then_avaliacao_adicionada(context):
    response = context['response']
    assert response.status_code == 200
    avaliacao = response.data
    assert avaliacao["nota"] == context['avaliacao_data']["nota"]
    assert avaliacao["comentario"] == context['avaliacao_data']["comentario"]

# @given(parsers.cfparse('Dado uma reserva no meu nome de endereço "{endereco}"'))
# def given_reserva_dono(context, endereco: str):
#     context['endereco'] = endereco

# @given(parsers.cfparse('Dado um comentário na reserva de ID "{comentario_id:d}" que desejo ocultar'))
# def given_comentario(context, comentario_id: int):
#     context['comentario_id'] = comentario_id

# @when('Eu coloco para ocultar tal comentário')
# def when_ocultar_comentario(context):
#     context['response'] = ReviewService.hide_review(context['cpfnj'], context['comentario_id'])

# @then('O comentário é definido como ocultado')
# def then_comentario_ocultado(context):
#     response = context['response']
#     assert response.status_code == 200
#     assert response.json() == {"message": "Avaliação marcada como oculta"}

#     # Verificar se o comentário foi realmente ocultado no banco de dados
#     db_ava = ReviewService.get_all_reviews()
#     avaliacao = next((a for a in db_ava if a["id"] == context['comentario_id']), None)
#     assert avaliacao is not None
#     assert avaliacao["oculto"] is True