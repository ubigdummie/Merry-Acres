from cryptography.fernet import Fernet


def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def encrypt_credentials(credentials):
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)
    encrypted = f.encrypt(credentials.encode())
    with open("credentials.enc", "wb") as enc_file:
        enc_file.write(encrypted)


def decrypt_credentials():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    f = Fernet(key)
    with open("credentials.enc", "rb") as enc_file:
        encrypted = enc_file.read()
    return f.decrypt(encrypted).decode()


# Example usage
if __name__ == "__main__":
    generate_key()
    encrypt_credentials("admin:password123")
    print(decrypt_credentials())
