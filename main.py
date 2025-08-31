# main.py — Menu interativo de Login Seguro
import time
from security import hash_password, verify_password
from storage import load_db, save_db, create_user, get_user, set_password, mark_fail, reset_fail

MAX_ATTEMPTS = 3
LOCK_SECONDS = 30

def register():
    db = load_db()
    username = input("Digite o nome de usuário: ")
    if get_user(db, username):
        print("⚠ Usuário já existe. Escolha outro.")
        return
    password = input("Digite a senha: ")
    hpwd = hash_password(password)
    create_user(db, username, hpwd)
    save_db(db)
    print(f"✅ Usuário {username} criado com sucesso.\n")

def login():
    db = load_db()
    username = input("Digite o nome de usuário: ")
    u = get_user(db, username)
    if not u:
        print("⚠ Usuário não existe.\n")
        return
    now = int(time.time())
    if u["lock_until"] and now < u["lock_until"]:
        print(f"⛔ Conta bloqueada. Tente novamente em {u['lock_until']-now}s.\n")
        return

    password = input("Digite a senha: ")
    if verify_password(u["password_hash"], password):
        reset_fail(db, username)
        save_db(db)
        print("✅ Login bem-sucedido!\n")
    else:
        mark_fail(db, username, MAX_ATTEMPTS, LOCK_SECONDS)
        save_db(db)
        print("❌ Senha incorreta.\n")

def change_password():
    db = load_db()
    username = input("Digite o nome de usuário: ")
    u = get_user(db, username)
    if not u:
        print("⚠ Usuário não existe.\n")
        return
    current = input("Digite a senha atual: ")
    if not verify_password(u["password_hash"], current):
        print("❌ Senha atual incorreta.\n")
        return
    new = input("Digite a nova senha: ")
    set_password(db, username, hash_password(new))
    save_db(db)
    print("✅ Senha alterada com sucesso.\n")

def main():
    while True:
        print("=== MENU LOGIN SEGURO ===")
        print("1. Registrar novo usuário")
        print("2. Fazer login")
        print("3. Alterar senha")
        print("4. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            change_password()
        elif choice == "4":
            print("👋 Encerrando...")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    main()
