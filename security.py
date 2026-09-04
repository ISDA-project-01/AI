import os
import hashlib
import hmac
import secrets

def generate_token(length=32):
    return secrets.token_hex(length)

def hash_password(password: str, salt: str = None) -> tuple:
    if not salt:
        salt = secrets.token_hex(16)
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt.encode('utf-8'),
        100000
    ).hex()
    return hashed, salt

def verify_password(password: str, hashed: str, salt: str) -> bool:
    new_hash, _ = hash_password(password, salt)
    return hmac.compare_digest(new_hash, hashed)

def sanitize_filename(filename: str) -> str:
    filename = os.path.basename(filename)
    clean_name = "".join(c for c in filename if c.isalnum() or c in "._- ")
    return clean_name or "file.bin"

def is_safe_path(base_dir: str, target_path: str) -> bool:
    abs_base = os.path.abspath(base_dir)
    abs_target = os.path.abspath(target_path)
    return abs_target.startswith(abs_base)
