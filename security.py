# security.py — hashing de senhas com Argon2
from argon2 import PasswordHasher

ph = PasswordHasher(time_cost=2, memory_cost=51200, parallelism=2)

def hash_password(plain: str) -> str:
    return ph.hash(plain)

def verify_password(hash_str: str, plain: str) -> bool:
    try:
        ph.verify(hash_str, plain)
        return True
    except Exception:
        return False
