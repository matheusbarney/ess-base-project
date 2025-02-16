Feature: Avaliação de reservas

Scenario: Avaliar reserva durante minha estadia, com um comentário pessoal.
    Given Sou o usuário "Heisenberg" de CPF "9"
    And Estou na reserva de endereço "Totó, PE"
    And Marco minha "Avaliação" como "5" estrelas e um comentário "Say my name."
    When Eu envio a avaliação
    Then A avaliação é adicionada com sucesso

Scenario: Eu sendo dono de uma reserva, ocultar comentário deixado na página da minha reserva.
    Given Sou o usuário "Hank Schrader" de CPF "1"
    And Dado uma reserva no meu nome de endereço "Totó, PE"
    And Dado um comentário na reserva de ID "2" que desejo ocultar
    When Eu coloco para ocultar tal comentário
    Then O comentário é definido como ocultado