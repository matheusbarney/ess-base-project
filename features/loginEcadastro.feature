<<<<<<< HEAD
Scenario: Usuário realiza o cadastro como pessoa física

Given que o usuário acessa a página de “Cadastro” 
When o usuário preenche os campos obrigatórios:   
| Tipo de Cadastro      | Pessoa Física
| Nome                         | "Bruno Teste Silva" 
| CPF                            | "123.456.789-00" 
| Data de nascimento | "11/07/2000" 
| UF                              | "SP" 
| Email                         | "bruno.teste@exa.com"  
| Login                         | "brunoteste" 
| Senha                        | "senhaExempl@" 
And clica em "Cadastrar" 
Then o sistema exibe a mensagem "Cadastro realizado com sucesso" 
And o sistema envia um email de confirmação para "bruno.teste@exa.com" 
And o usuário é redirecionado para a página inicial logado com seu perfil

Scenario: O usuário tenta se cadastrar com uma senha que não atende aos critérios de segurança 
Given que o usuário acessa a página de “cadastro” 
When o usuário preenche os campos obrigatórios:   
| Tipo de Cadastro      | Pessoa Física
| Nome                         | "Bruno Teste Silva" 
| CPF                            | "123.456.789-00" 
| Data de nascimento | "11/07/2000" 
| UF                              | "SP" 
| Email                         | "bruno.teste@exa.com"  
| Login                         | "brunoteste" 
| Senha                        | "seenha" 
And o usuário inseriu uma “senha” que não atende aos critérios 
And clica em "Cadastrar" 
Then o sistema exibe a mensagem de erro "A senha deve conter pelo menos 8 caracteres, incluindo letras e números" 
And o cadastro não é concluído 
And o usuário permanece na página de “Cadastro”.

Scenario: O usuário tenta se cadastrar com um email já cadastrado
Given que o usuário acessa a página de “Cadastro”
When o usuário preenche os campos obrigatórios:   
| Tipo de Cadastro      | Pessoa Física
| Nome                         | "Bruno Teste Silva" 
| CPF                            | "123.456.789-00" 
| Data de nascimento | "11/07/2000" 
| UF                              | "SP" 
| Email                         | "bruno.teste@exa.com"  
| Login                         | "brunoteste" 
| Senha                        | "senha123" 
And o usuário inseriu um “email” que já está registrado
And clica em "Cadastrar"
Then o sistema exibe a mensagem de erro "Este email já está em uso" 
And o cadastro não é concluído 
And o usuário permanece na página de “Cadastro”.

=======
>>>>>>> b5e2f9ef2ac4bbf3cbc50a171d0b5991aacbe989

