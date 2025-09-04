# main.py — Menu interativo de Login Seguro com cores
from app import register_user, login_user, change_password, list_users
from colorama import Fore, Style, init

# Inicializa o Colorama
init(autoreset=True)

def menu():
    while True:
        print(Fore.CYAN + "\n=== MENU LOGIN SEGURO ===")
        print(Fore.YELLOW + "1. Registrar novo usuário")
        print(Fore.YELLOW + "2. Fazer login")
        print(Fore.YELLOW + "3. Alterar senha")
        print(Fore.YELLOW + "4. Listar usuários")
        print(Fore.YELLOW + "5. Sair")

        choice = input(Fore.CYAN + "Escolha uma opção: " + Style.RESET_ALL)

        if choice == "1":
            user = input("Usuário: ")
            pwd = input("Senha: ")
            ok, msg = register_user(user, pwd)
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
                for u in users:
                    print(Fore.WHITE + f"- {u}")
            else:
                print(Fore.RED + "⚠ Nenhum usuário cadastrado.")

        elif choice == "5":
            print(Fore.MAGENTA + "👋 Encerrando...")
            break

        else:
            print(Fore.RED + "⚠ Opção inválida.")

if __name__ == "__main__":
    menu()
