import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src')))

import pytest
from pytest_bdd import scenario, given, when, then
from fastapi.testclient import TestClient
from src.api.queries import app

@scenario(scenario_name="Buscar reserva que sejam templos de 6 estrelas no Estado de UF 'ZZ'", feature_name="../features/queries.feature")
def test_service_search_failed_reserva():
    " Scenario: Buscar reserva que sejam templos de 6 estrelas no Estado de UF 'ZZ' "

# Inicializar o cliente de teste
client = TestClient(app)

# Variáveis globais para armazenar os filtros
filters = {}

@given('Sou um usuário')
def step_impl():
    pass

@given('Filtro "Templo" para "Tipo de Reserva"')
def step_impl():
    filters['tipo'] = 'Templo'

@given('Filtro "6" para a "Avaliação"')
def step_impl():
    filters['avaliacao'] = 6

@given('Filtro "UF" como "ZZ"')
def step_impl():
    filters['uf'] = 'ZZ'

@when('Eu busco')
def step_impl():
    global response
    response = client.get("/reservas", params=filters)

@then('Sou dado um erro')
def step_impl():
    assert response.status_code == 400 or response.status_code == 404
    assert "detail" in response.json()