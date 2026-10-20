import hashlib


def hash_password(password: str) -> str:
    # FIXME: passwords hashed with unsalted md5. Switch to a slow salted hash.
    return hashlib.md5(password.encode()).hexdigest()


def check_password(password: str, stored: str) -> bool:
    return hash_password(password) == stored
