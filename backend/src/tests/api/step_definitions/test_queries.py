import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src')))

import pytest
from pytest_bdd import scenario, given, when, then, parsers
from fastapi.testclient import TestClient
from src.service.impl.queries_service import QueriesService
from src.api.queries import app
from src.db.database import database

@scenario(scenario_name="Buscar reservas em Recife que sejam casas pet friendly e destacadas", feature_name="../features/queries.feature")
def test_service_search_reserva():
    " Scenario: Buscar reservas em Recife que sejam casas pet friendly e destacadas "

@scenario(scenario_name="Buscar reservas em SP que sejam de no mínimo 50 reais e no máximo 150 reais, e tenham avaliação acima de 3 estrelas", feature_name="../features/queries.feature")
def test_service_search_reserva_sp():
    " Scenario: Buscar reservas em SP que sejam de no mínimo 50 reais e no máximo 150 reais, e tenham avaliação acima de 3 estrelas "

# Inicializar o cliente de teste
client = TestClient(app)

# Variáveis globais para armazenar os filtros
filters = {}

@given('Sou um usuário')
def given_user():
    pass

@given(parsers.cfparse('Filtro "UF" como "{uf}"'))
def given_filter_uf(uf: str):
    filters['uf'] = uf

@given(parsers.cfparse('Filtro "{tipo}" para "Tipo de Reserva"'))
def given_filter_tipo(tipo: str):
    filters['tipo'] = tipo

@given(parsers.cfparse('Filtro "{petfriendly}" para "Pet Friendly"'))
def given_filter_petfriendly(petfriendly: str):
    filters['petfriendly'] = petfriendly.lower() == 'sim'

@given(parsers.cfparse('Filtro "{destacado}" para "Destacado"'))
def given_filter_destacado(destacado: str):
    filters['destacado'] = destacado.lower() == 'sim'

@given(parsers.cfparse('Filtro "{valmin:d}" para "Valor Mínimo"'))
def given_filter_valmin(valmin: int):
    filters['valmin'] = valmin

@given(parsers.cfparse('Filtro "{valmax:d}" para "Valor Máximo"'))
def given_filter_valmax(valmax: int):
    filters['valmax'] = valmax

@given(parsers.cfparse('Filtro "{avaliacao:d}" para "Avaliação"'))
def given_filter_avaliacao(avaliacao: int):
    filters['avaliacao'] = avaliacao

@when('Eu busco', target_fixture="context")
def when_search(context):
    context['response'] = QueriesService.get_queries(filters)
    return context

@then('Sou dado uma lista filtrada de reservas, ou uma alerta caso não exista', target_fixture="context")
def then_check_response(context):
    response = context['response']
    if response.status_code == 404:
        assert response.model_dump_json() == '{"message":"No reservations found with the given filters","status_code":404,"data":null}'
    else:
        assert response.status_code == 200
        reservas = response.data
        assert isinstance(reservas, list)
        for reserva in reservas:
            if 'uf' in filters:
                assert reserva['endereco'].endswith(filters['uf'])
            if 'tipo' in filters:
                assert reserva['tipo'].lower() == filters['tipo'].lower()
            if 'petfriendly' in filters:
                assert reserva['petfriendly'] is filters['petfriendly']
            if 'destacado' in filters:
                assert reserva['destacado'] is filters['destacado']
            if 'valmin' in filters:
                assert reserva['preco'] >= filters['valmin']
            if 'valmax' in filters:
                assert reserva['preco'] <= filters['valmax']
            if 'avaliacao' in filters:
                assert reserva['avalMedia'] >= float(filters['avaliacao'])
    return context
