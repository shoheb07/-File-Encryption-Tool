from cryptography.fernet import Fernet
from key_manager import load_key


def encrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted_data)

    print("File encrypted successfully.")
