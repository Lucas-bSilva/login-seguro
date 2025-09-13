# Arquivo implementa o menu principal do sistema Login Seguro,
# Permite que o usuário interaja com as funcionalidades disponíveis.
# Técnica principal: hashing criptográfico com bcrypt, que transforma as senhas em valores irreversíveis e únicos 
# (mesmo que duas pessoas usem a mesma senha, os resultados ficam diferentes por conta do sal). 
# Evita que senhas fiquem expostas em caso de vazamento do banco de dados.
# O sistema conta com um mecanismo de bloqueio temporário após múltiplas tentativas falhas de login (account lockout), 
# protegendo contra ataques de força bruta (quando alguém tenta adivinhar a senha testando várias combinações).

from app import (
    register_user, login_user, change_password,
    list_users, delete_user, delete_all_users,
    list_password_hashes
)
from colorama import Fore, Style, init

# Inicializa o Colorama para permitir uso de cores no terminal
init(autoreset=True)

# Nome fictício da empresa de TI focada em segurança
COMPANY_NAME = "Soluções em Segurança da Informação"

def menu():
    # Loop principal do menu (executa até o usuário escolher sair)
    while True:
        # Exibição do menu com cores + nome da empresa
        print(Fore.CYAN + f"\n=== MENU LOGIN SEGURO - {COMPANY_NAME} ===")
        print(Fore.YELLOW + "1. Registrar novo usuário")
        print(Fore.YELLOW + "2. Fazer login")
        print(Fore.YELLOW + "3. Alterar senha")
        print(Fore.YELLOW + "4. Listar usuários")
        print(Fore.YELLOW + "5. Excluir usuário")
        print(Fore.YELLOW + "6. Excluir todos os usuários")
        print(Fore.YELLOW + "7. Mostrar senhas criptografadas")
        print(Fore.YELLOW + "8. Sair")

        # Captura da opção escolhida
        choice = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL)

        # 1 - Registro de novo usuário
        if choice == "1":
            user = input("Usuário: ")
            cargo = input("Cargo na empresa: ")
            pwd = input("Senha: ")
            ok, msg = register_user(user, pwd, cargo)
            print(Fore.GREEN + msg if ok else Fore.RED + msg)

        # 2 - Login de usuário
        elif choice == "2":
            user = input("Usuário: ")
            pwd = input("Senha: ")
            ok, msg = login_user(user, pwd)
            print(Fore.GREEN + msg if ok else Fore.RED + msg)

        # 3 - Alteração de senha
        elif choice == "3":
            user = input("Usuário: ")
            current = input("Senha atual: ")
            new = input("Nova senha: ")
            ok, msg = change_password(user, current, new)
            print(Fore.GREEN + msg if ok else Fore.RED + msg)

        # 4 - Listagem de usuários cadastrados
        elif choice == "4":
            users = list_users()
            if users:
                print(Fore.CYAN + "\n👥 Usuários cadastrados:")
                for u, cargo in users:
                    print(Fore.WHITE + f"- {u} ({cargo})")
            else:
                print(Fore.RED + "⚠ Nenhum usuário cadastrado.")

        # 5 - Exclusão de usuário específico
        elif choice == "5":
            user = input("Digite o nome do usuário a excluir: ")
            ok, msg = delete_user(user)
            print(Fore.GREEN + msg if ok else Fore.RED + msg)

        # 6 - Exclusão de todos os usuários (com confirmação)
        elif choice == "6":
            confirm = input("Tem certeza que deseja excluir TODOS os usuários? (s/n): ")
            if confirm.lower() == "s":
                ok, msg = delete_all_users()
                print(Fore.GREEN + msg if ok else Fore.RED + msg)
            else:
                print(Fore.YELLOW + "⚠ Operação cancelada.")

        # 7 - Mostrar as senhas criptografadas (apenas para demonstração)
        elif choice == "7":
            hashes = list_password_hashes()
            if hashes:
                print(Fore.CYAN + "\n🔐 Senhas criptografadas (hashes):")
                for user, h in hashes:
                    print(Fore.WHITE + f"- {user}: {h}")
            else:
                print(Fore.RED + "⚠ Nenhum usuário cadastrado.")

        # 8 - Encerrar o programa
        elif choice == "8":
            print(Fore.MAGENTA + f"👋 Encerrando o sistema da {COMPANY_NAME}...")
            break

        # Opção inválida
        else:
            print(Fore.RED + "⚠ Opção inválida.")

# Ponto de entrada do programa
if __name__ == "__main__":
    menu()
