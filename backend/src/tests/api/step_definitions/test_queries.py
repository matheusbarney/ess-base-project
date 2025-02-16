import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'src')))

import pytest
from pytest_bdd import scenario, given, when, then
from fastapi.testclient import TestClient
from src.api.queries import app

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
def step_impl():
    pass

@given('Filtro "UF" como "PE"')
def step_impl():
    filters['uf'] = 'PE'

@given('Filtro "Casa" para "Tipo de Reserva"')
def step_impl():
    filters['tipo'] = 'Casa'

@given('Filtro "Sim" para "Pet Friendly"')
def step_impl():
    filters['petfriendly'] = True

@given('Filtro "Sim" para "Destacado"')
def step_impl():
    filters['destacado'] = True

@given('Filtro "UF" como "SP"')
def step_impl():
    filters['uf'] = 'SP'

@given('Filtro "50" para "Valor Mínimo"')
def step_impl():
    filters['valmin'] = 50

@given('Filtro "150" para "Valor Máximo"')
def step_impl():
    filters['valmax'] = 150

@given('Filtro "3" para "Avaliação"')
def step_impl():
    filters['avaliacao'] = 3

@when('Eu busco')
def step_impl():
    global response
    response = client.get("/reservas", params=filters)

@then('Sou dado uma lista filtrada de reservas, ou uma alerta caso não exista')
def step_impl():
    if response.status_code == 404:
        assert response.json() == {"detail": "Nenhuma reserva encontrada dentro desses filtros"}
    else:
        assert response.status_code == 200
        reservas = response.json()
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
