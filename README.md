## Descrição

O Login Seguro é um sistema de autenticação de usuários desenvolvido em Python, como parte da disciplina de Segurança Computacional.

O projeto aplica boas práticas de segurança, como:

Armazenamento de senhas com hashing criptográfico (Argon2/Bcrypt), garantindo que nenhuma senha seja salva em texto puro.

Bloqueio temporário automático após 3 tentativas consecutivas de login incorretas, protegendo contra ataques de força bruta.

Cadastro de usuários com cargo associado, simulando um ambiente corporativo (ex.: cadastro de funcionários de uma empresa de TI).

Exibição opcional das senhas criptografadas (hashes), apenas para fins de demonstração acadêmica.

O sistema oferece um menu interativo no terminal, identificado pelo nome fictício da empresa “Soluções em Segurança da Informação”, permitindo o gerenciamento de usuários de forma simples e segura.

## Requisitos

Python 3.10+

Pip atualizado

Bibliotecas listadas em requirements.txt:

bcrypt

colorama

## Instalação

Na raiz do projeto, execute:

pip install -r requirements.txt

## Como executar

No terminal, dentro da pasta do projeto, rode:

python main.py


Será exibido o menu interativo:

=== MENU LOGIN SEGURO - Soluções em Segurança da Informação ===
1. Registrar novo usuário
2. Fazer login
3. Alterar senha
4. Listar usuários
5. Excluir usuário
6. Excluir todos os usuários
7. Mostrar senhas criptografadas
8. Sair

## Funcionalidades
1. Registrar usuário

Cria um novo cadastro, incluindo nome, cargo e senha.

Impede duplicação de nomes de usuário.

2. Fazer login

Valida o usuário e a senha.

Após 3 erros consecutivos, o login é bloqueado temporariamente.

3. Alterar senha

Permite trocar a senha apenas mediante validação da senha atual.

4. Listar usuários

Mostra todos os usuários cadastrados com seus respectivos cargos.

5. Excluir usuário

Remove um usuário específico do banco de dados.

6. Excluir todos os usuários

Limpa completamente o banco de usuários.

7. Mostrar senhas criptografadas

Exibe os hashes das senhas cadastradas (apenas para fins de estudo e demonstração).

8. Sair

Encerra a execução do sistema.

## Estrutura do projeto
login-seguro/
│-- app.py             # Funções principais (cadastro, login, senha, exclusão, listagem, hashes)
│-- security.py        # Hashing e verificação de senhas (Argon2/Bcrypt)
│-- storage.py         # Armazenamento simples em JSON
│-- main.py            # Menu interativo colorido no terminal com nome fictício da empresa
│-- requirements.txt   # Dependências do projeto
│-- README.md          # Documentação do projeto
│-- db.json            # Banco de dados simples em JSON (gerado automaticamente)