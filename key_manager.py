from cryptography.fernet import Fernet
import os

KEY_FOLDER = "keys"
KEY_FILE = os.path.join(KEY_FOLDER, "secret.key")


def generate_key():
    os.makedirs(KEY_FOLDER, exist_ok=True)
    key = Fernet.generate_key()

    with open(KEY_FILE, "wb") as file:
        file.write(key)

    print("Key generated successfully.")


def load_key():
    with open(KEY_FILE, "rb") as file:
        return file.read()


if __name__ == "__main__":
    generate_key()
