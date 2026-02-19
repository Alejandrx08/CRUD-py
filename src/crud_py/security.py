import bcrypt

def hash_password(password):
    passbyte = password.encode()
    salt = bcrypt.gensalt()
    hashbyte = bcrypt.hashpw(passbyte, salt)
    return hashbyte.decode()


def verify_password(password, password_hash):
    passinput = password.encode()
    hashguardado = password_hash.encode()

    count = bcrypt.checkpw(passinput, hashguardado)
    return count
