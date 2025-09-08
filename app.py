# app.py — Funções principais de cadastro/login
# Este arquivo contém as funções centrais que controlam
# o fluxo de autenticação e gerenciamento de usuários.

import time
from security import hash_password, verify_password
from storage import load_db, save_db, create_user, get_user, set_password, mark_fail, reset_fail

# Configurações globais do sistema de login
MAX_ATTEMPTS = 3   # número máximo de tentativas falhas antes de bloquear o login
LOCK_SECONDS = 30  # tempo de bloqueio (em segundos) após atingir o limite de falhas

def register_user(username: str, password: str):
    """
    Registra um novo usuário no sistema, desde que ele ainda não exista.
    - Recebe nome de usuário e senha em texto puro.
    - Converte a senha em hash seguro antes de salvar.
    """
    db = load_db()
    if get_user(db, username):
        return False, "⚠ Usuário já existe."
    hpwd = hash_password(password)
    create_user(db, username, hpwd)
    save_db(db)
    return True, f"✅ Usuário {username} criado com sucesso."

def login_user(username: str, password: str):
    """
    Realiza a autenticação do usuário.
    - Se o usuário não existe, retorna erro.
    - Se houver falhas consecutivas, aplica bloqueio temporário.
    - Se a senha estiver correta, reseta as falhas e autoriza o login.
    """
    db = load_db()
    u = get_user(db, username)
    if not u:
        return False, "⚠ Usuário não existe."
    
    now = int(time.time())
    # Verifica se o usuário está bloqueado
    if u["lock_until"] and now < u["lock_until"]:
        return False, f"⛔ Conta bloqueada. Tente novamente em {u['lock_until']-now}s."
    
    # Valida a senha
    if verify_password(u["password_hash"], password):
        reset_fail(db, username)   # reseta falhas após login correto
        save_db(db)
        return True, "✅ Login bem-sucedido!"
    else:
        # Incrementa contador de falhas e aplica bloqueio se necessário
        mark_fail(db, username, MAX_ATTEMPTS, LOCK_SECONDS)
        save_db(db)

        # Recarrega o usuário após a tentativa para verificar se foi bloqueado
        u = get_user(db, username)
        now = int(time.time())
        if u["lock_until"] and now < u["lock_until"]:
            return False, f"⛔ Conta bloqueada. Tente novamente em {u['lock_until']-now}s."
        
        return False, "❌ Senha incorreta."

def change_password(username: str, current: str, new: str):
    """
    Permite que um usuário altere sua senha.
    - Verifica se o usuário existe.
    - Confere a senha atual antes de permitir a alteração.
    - Armazena a nova senha de forma segura (hash).
    """
    db = load_db()
    u = get_user(db, username)
    if not u:
        return False, "⚠ Usuário não existe."
    if not verify_password(u["password_hash"], current):
        return False, "❌ Senha atual incorreta."
    set_password(db, username, hash_password(new))
    save_db(db)
    return True, "✅ Senha alterada com sucesso."

def list_users():
    """
    Lista todos os usuários cadastrados no banco de dados.
    Retorna uma lista com os nomes.
    """
    db = load_db()
    return list(db["users"].keys())

def delete_user(username: str):
    """
    Exclui um usuário específico do banco de dados.
    - Verifica se o usuário existe antes de remover.
    """
    db = load_db()
    u = get_user(db, username)
    if not u:
        return False, "⚠ Usuário não existe."
    del db["users"][username]
    save_db(db)
    return True, f"✅ Usuário {username} removido com sucesso."

def delete_all_users():
    """
    Exclui todos os usuários cadastrados no banco.
    - Se não houver usuários, retorna aviso.
    """
    db = load_db()
    if not db["users"]:
        return False, "⚠ Nenhum usuário cadastrado."
    db["users"].clear()
    save_db(db)
    return True, "✅ Todos os usuários foram removidos com sucesso."
