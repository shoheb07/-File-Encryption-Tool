from cryptography.fernet import Fernet
from key_manager import load_key


def decrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    output_file = file_path.replace(".enc", "")

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print("File decrypted successfully.")
