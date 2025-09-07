# 🔐 Projeto – Login Seguro

## 📖 Descrição
O Login Seguro é um sistema de autenticação de usuários desenvolvido em Python como parte da disciplina de Segurança Computacional.
O projeto aplica boas práticas de segurança, como armazenamento de senhas com hashing criptográfico (bcrypt), garantindo que nenhuma senha seja armazenada em texto puro. Além disso, conta com bloqueio temporário automático após três tentativas consecutivas de login incorretas, protegendo contra ataques de força bruta.

O sistema oferece um menu interativo no terminal, permitindo o gerenciamento de usuários de forma simples e segura. Ele é um exemplo prático de como técnicas de segurança vistas na disciplina podem ser aplicadas em implementações reais. 

---

# ⚙️ Requisitos

Python 3.10+

Pip atualizado

Bibliotecas listadas em requirements.txt:

bcrypt

colorama

# 📦 Instalação
Na raiz do projeto, execute:
pip install -r requirements.txt


▶️ Como executar

No terminal, dentro da pasta do projeto, rode:

python main.py

Será exibido o menu interativo:

=== MENU LOGIN SEGURO ===
1. Registrar novo usuário
2. Fazer login
3. Alterar senha
4. Listar usuários
5. Excluir usuário
6. Excluir todos os usuários
7. Sair

🛠️ Funcionalidades

1 - Registrar usuário

Cria um novo cadastro, impedindo duplicação de nomes.

2 - Login

Valida o usuário e a senha.

Em caso de 3 erros consecutivos, o login é bloqueado temporariamente.

3 - Alterar senha

Permite trocar a senha apenas mediante validação da senha atual.

4 - Listar usuários

Mostra todos os usuários cadastrados no sistema.

5 - Excluir usuário

Remove um usuário específico do banco de dados.

6 - Excluir todos os usuários

Limpa completamente o banco de usuários.

7 - Sair

Encerra a execução do sistema.


📂 Estrutura do projeto

login-seguro/
│-- app.py                # Funções principais (cadastro, login, senha, exclusão, listagem)
│-- security.py           # Hashing e verificação de senhas
│-- storage.py            # Armazenamento simples em JSON
│-- main.py               # Menu interativo colorido no terminal
│-- requirements.txt      # Dependências do projeto
│-- README.md             # Documentação do projeto

