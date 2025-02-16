Feature: Busca de Reservas

Scenario: Buscar reservas em Recife que sejam casas pet friendly e destacadas
    Given Sou um usuário
    And Filtro "UF" como "PE"
    And Filtro "Casa" para "Tipo de Reserva"
    And Filtro "Sim" para "Pet Friendly"
    And Filtro "Sim" para "Destacado"
    When Eu busco
    Then Sou dado uma lista filtrada de reservas, ou uma alerta caso não exista

Scenario: Buscar reservas em SP que sejam de no mínimo 50 reais e no máximo 150 reais, e tenham avaliação acima de 3 estrelas
    Given Sou um usuário
    And Filtro "UF" como "SP"
    And Filtro "50" para "Valor Mínimo"
    And Filtro "150" para "Valor Máximo"
    And Filtro "3" para "Avaliação"
    When Eu busco
    Then Sou dado uma lista filtrada de reservas, ou uma alerta caso não exista

Scenario: Buscar reserva que sejam templos de 6 estrelas no Estado de UF 'ZZ'
    Given Sou um usuário
    And Filtro "Templo" para "Tipo de Reserva"
    And Filtro "6" para a "Avaliação"
    And Filtro "UF" como "ZZ"
    When Eu busco
    Then Sou dado um erro