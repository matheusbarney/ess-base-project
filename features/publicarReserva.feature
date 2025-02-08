Scenario: Usuário tenta acessar o formulário de publicação sem confirmar o email

Given que o usuário está logado como “usuário não-anfitrião”
And o email do usuário está pendente de confirmação
When o usuário "Adicionar Locação"
Then o sistema exibe um pop-up com a mensagem "Você precisa confirmar seu email antes de publicar uma reserva. Por favor, verifique sua caixa de entrada ou clique aqui para reenviar o email de confirmação."
And o usuário permanece na mesma página

Scenario: Usuário publicar uma reserva 
   
Given que o usuário tem permissão de “anfitrião”
And acessa a página "Adicionar Locação"
When o usuário preenche os campos obrigatórios:                           
      | Título                 | "Casa Aconchegante"      
      | Descrição          | "Uma bela casa a poucos metros de mercados, farmácias e parques
      | Imagens            | ["https://exemplo.com/imagem1.jpg"] 
      | Petfriendly        | "Não"                            
      | Endereço           | "Av. Jorn. Aníbal Fernandes, São Paulo" 
      | Tipo                   | "Residencial"              
      | Disponibilidade | "Segunda a Sexta-feira" 
      | Preço                 | "R$ 150,00"                      
And clica em "Publicar"
Then o sistema exibe a mensagem "Reserva publicada com sucesso"
And a reserva aparece como ativa na página de reservas do anfitrião
