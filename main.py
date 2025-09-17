"""
===============================================================
Projeto: Login Seguro – Sistema de Autenticação de Usuários
===============================================================

Este projeto é um exemplo prático de sistema de autenticação 
desenvolvido em Python, simulando um ambiente profissional, 
como o cadastro e gerenciamento de funcionários de uma 
empresa de TI (por exemplo, a ProtecTI Solutions).

O sistema implementa:
- Cadastro de usuários com nome, cargo e e-mail.
- Armazenamento seguro de senhas usando hashing criptográfico 
  com bcrypt, garantindo que as senhas não fiquem em texto puro.
- Sal integrado no bcrypt: mesmo senhas iguais resultam em 
  hashes diferentes.
- Mecanismo de bloqueio temporário (account lockout) após 
  múltiplas tentativas incorretas, protegendo contra ataques 
  de força bruta.

Mecanismos de segurança aplicados:
- Hashing criptográfico (bcrypt) para proteção de credenciais.
- Bloqueio automático de contas após tentativas falhas.
- Armazenamento local dos dados em JSON (db.json), 
  simulando um pequeno banco de dados seguro.

Este projeto pode ser usado como analogia de um sistema 
real de controle de acesso para funcionários, onde as 
credenciais e permissões precisam ser protegidas de forma 
confiável contra vazamentos ou ataques externos.
===============================================================
"""

from app import (
    register_user, login_user, change_password,
    list_users, delete_user, delete_all_users,
    list_password_hashes
)
from colorama import Fore, Style, init

# Inicializa o Colorama para permitir uso de cores no terminal
init(autoreset=True)

# Nome da empresa de TI focada em segurança
COMPANY_NAME = "Soluções em Segurança da Informação"

def menu():
    while True:
        print(Fore.CYAN + f"\n=== MENU LOGIN SEGURO - {COMPANY_NAME} ===")
        print(Fore.YELLOW + "1. Registrar novo usuário")
        print(Fore.YELLOW + "2. Fazer login")
        print(Fore.YELLOW + "3. Alterar senha")
        print(Fore.YELLOW + "4. Listar usuários")
        print(Fore.YELLOW + "5. Excluir usuário")
        print(Fore.YELLOW + "6. Excluir todos os usuários")
        print(Fore.YELLOW + "7. Mostrar senhas criptografadas")
        print(Fore.YELLOW + "8. Sair")

        choice = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL)

        if choice == "1":
            user = input("Usuário: ")
            email = input("E-mail corporativo: ")
            cargo = input("Cargo na empresa: ")
            pwd = input("Senha: ")
            ok, msg = register_user(user, pwd, cargo, email)
            print(Fore.GREEN + msg if ok else Fore.RED + msg)

        elif choice == "2":
            user = input("Usuário: ")
            pwd = input("Senha: ")
            ok, msg = login_user(user, pwd)
            print(Fore.GREEN + msg if ok else Fore.RED + msg)

        elif choice == "3":
            user = input("Usuário: ")
            current = input("Senha atual: ")
            new = input("Nova senha: ")
            ok, msg = change_password(user, current, new)
            print(Fore.GREEN + msg if ok else Fore.RED + msg)

        elif choice == "4":
            users = list_users()
            if users:
                print(Fore.CYAN + "\n👥 Usuários cadastrados:")
                for u, cargo, email in users:
                    print(Fore.WHITE + f"- {u} | {cargo} | {email}")
            else:
                print(Fore.RED + "⚠ Nenhum usuário cadastrado.")

        elif choice == "5":
            user = input("Digite o nome do usuário a excluir: ")
            ok, msg = delete_user(user)
            print(Fore.GREEN + msg if ok else Fore.RED + msg)

        elif choice == "6":
            confirm = input("Tem certeza que deseja excluir TODOS os usuários? (s/n): ")
            if confirm.lower() == "s":
                ok, msg = delete_all_users()
                print(Fore.GREEN + msg if ok else Fore.RED + msg)
            else:
                print(Fore.YELLOW + "⚠ Operação cancelada.")

        elif choice == "7":
            hashes = list_password_hashes()
            if hashes:
                print(Fore.CYAN + "\n🔐 Senhas criptografadas (hashes):")
                for user, h in hashes:
                    print(Fore.WHITE + f"- {user}: {h}")
            else:
                print(Fore.RED + "⚠ Nenhum usuário cadastrado.")

        elif choice == "8":
            print(Fore.MAGENTA + f"👋 Encerrando o sistema da {COMPANY_NAME}...")
            break

        else:
            print(Fore.RED + "⚠ Opção inválida.")

if __name__ == "__main__":
    menu()
