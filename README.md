# 🔐 Projeto 1 – Login Seguro

## 📖 Descrição
O Projeto 1 – Login Seguro tem como objetivo implementar um sistema de autenticação de usuários utilizando técnicas de segurança estudadas na disciplina de Segurança Computacional. As senhas não são armazenadas em texto puro, mas sim através de hashing criptográfico com a biblioteca `bcrypt`, que aplica um algoritmo de derivação de chave com sal integrado. Essa abordagem garante maior proteção mesmo em cenários de vazamento de credenciais.  

O sistema também implementa mecanismos de controle de acesso contra ataques de força bruta. O usuário possui no máximo três tentativas consecutivas de login; em caso de falha, sua conta é temporariamente bloqueada, reforçando a segurança do processo de autenticação. Dessa forma, o projeto alia teoria e prática, apresentando um exemplo funcional de boas práticas em autenticação e proteção de credenciais.  

---

## ⚙️ Requisitos
- Python **3.10+**
- Pip atualizado
- Biblioteca `bcrypt`

---

## 📦 Instalação
Na raiz do projeto, execute:
```bash
pip install -r requirements.txt

▶️ Como executar

No terminal, dentro da pasta login-seguro, rode:

python main.py

Será exibido o menu interativo:

=== MENU LOGIN SEGURO ===
1. Registrar novo usuário
2. Fazer login
3. Alterar senha
4. Sair

🛠️ Funcionalidades

1 - Registrar usuário
Cria um novo cadastro, impedindo a duplicação de nomes de usuário.

2 - Login
Valida o usuário e a senha, bloqueando a conta após três falhas consecutivas.

3 - Alterar senha
Permite a troca de senha mediante a verificação da senha atual.

4 - Sair
Encerra a execução do sistema.


📂 Estrutura do projeto

login-seguro/
│-- app.py          # Funções principais de cadastro, login e troca de senha
│-- security.py     # Módulo responsável pelo hashing e verificação de senhas
│-- storage.py      # Armazenamento simples em JSON
│-- main.py         # Interface de menu interativo para o usuário
│-- requirements.txt# Dependências do projeto
│-- README.md       # Documentação do projeto
