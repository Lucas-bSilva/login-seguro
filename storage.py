# storage.py — banco simples em JSON
import json, time
from pathlib import Path

DB_PATH = Path("db.json")

def _empty_db():
    return {"users": {}}

def load_db():
    if DB_PATH.exists():
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    return _empty_db()

def save_db(db):
    DB_PATH.write_text(json.dumps(db, indent=2, ensure_ascii=False), encoding="utf-8")

def get_user(db, username):
    return db["users"].get(username)

def create_user(db, username, pwd_hash):
    if username in db["users"]:
        raise ValueError("Usuário já existe.")
    db["users"][username] = {
        "password_hash": pwd_hash,
        "failed": 0,
        "lock_until": 0
    }

def set_password(db, username, pwd_hash):
    db["users"][username]["password_hash"] = pwd_hash
    db["users"][username]["failed"] = 0
    db["users"][username]["lock_until"] = 0

def mark_fail(db, username, max_attempts, lock_seconds):
    u = db["users"][username]
    u["failed"] += 1
    if u["failed"] >= max_attempts:
        u["lock_until"] = int(time.time()) + lock_seconds
        u["failed"] = 0

def reset_fail(db, username):
    u = db["users"][username]
    u["failed"] = 0
    u["lock_until"] = 0
