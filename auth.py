import os
from security import hash_password, verify_password, generate_token

sessions = {}

# Simple in-memory user registry (credentials initialized from env or defaults)
ADMIN_USER = os.getenv("VAPIC_ADMIN_USERNAME", "admin")
ADMIN_PASS = os.getenv("VAPIC_ADMIN_PASSWORD", "adminpassword123")
SUPERVISOR_USER = os.getenv("VAPIC_SUPERVISOR_USERNAME", "supervisor")
SUPERVISOR_PASS = os.getenv("VAPIC_SUPERVISOR_PASSWORD", "superpassword123")

admin_hash, admin_salt = hash_password(ADMIN_PASS)
sup_hash, sup_salt = hash_password(SUPERVISOR_PASS)

USERS = {
    ADMIN_USER: {"hash": admin_hash, "salt": admin_salt, "role": "admin"},
    SUPERVISOR_USER: {"hash": sup_hash, "salt": sup_salt, "role": "supervisor"}
}

def authenticate_user(username, password):
    user = USERS.get(username)
    if not user:
        return None
    if verify_password(password, user["hash"], user["salt"]):
        token = generate_token()
        sessions[token] = {"username": username, "role": user["role"]}
        return token
    return None

def verify_session(token):
    return sessions.get(token)

def revoke_session(token):
    sessions.pop(token, None)
