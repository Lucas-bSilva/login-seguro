# app.py — Funções principais de cadastro/login
import time
from security import hash_password, verify_password
from storage import load_db, save_db, create_user, get_user, set_password, mark_fail, reset_fail

MAX_ATTEMPTS = 3
LOCK_SECONDS = 30

def register_user(username: str, password: str):
    """Registra novo usuário se ainda não existir."""
    db = load_db()
    if get_user(db, username):
        return False, "⚠ Usuário já existe."
    hpwd = hash_password(password)
    create_user(db, username, hpwd)
    save_db(db)
    return True, f"✅ Usuário {username} criado com sucesso."

def login_user(username: str, password: str):
    """Tenta login, respeitando bloqueio e número de tentativas."""
    db = load_db()
    u = get_user(db, username)
    if not u:
        return False, "⚠ Usuário não existe."
    now = int(time.time())
    if u["lock_until"] and now < u["lock_until"]:
        return False, f"⛔ Conta bloqueada. Tente novamente em {u['lock_until']-now}s."
    if verify_password(u["password_hash"], password):
        reset_fail(db, username)
        save_db(db)
        return True, "✅ Login bem-sucedido!"
    else:
        mark_fail(db, username, MAX_ATTEMPTS, LOCK_SECONDS)
        save_db(db)
        return False, "❌ Senha incorreta."

def change_password(username: str, current: str, new: str):
    """Troca a senha do usuário se a atual for correta."""
    db = load_db()
    u = get_user(db, username)
    if not u:
        return False, "⚠ Usuário não existe."
    if not verify_password(u["password_hash"], current):
        return False, "❌ Senha atual incorreta."
    set_password(db, username, hash_password(new))
    save_db(db)
    return True, "✅ Senha alterada com sucesso."
