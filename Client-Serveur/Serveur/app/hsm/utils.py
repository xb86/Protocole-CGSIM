import hsm
def encrypt_data(data, key):
    # Utilisation d'une méthode d'encryptage avec la clé HSM
    encrypted = hsm.encrypt(data, key)
    return encrypted

def decrypt_data(encrypted_data, key):
    decrypted = hsm.decrypt(encrypted_data, key)
    return decrypted
