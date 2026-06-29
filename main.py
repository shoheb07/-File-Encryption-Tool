from encrypt import encrypt_file
from decrypt import decrypt_file
from key_manager import generate_key
import os

if not os.path.exists("keys/secret.key"):
    generate_key()

while True:
    print("\n===== File Encryption Tool =====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        path = input("Enter file path: ")
        encrypt_file(path)

    elif choice == "2":
        path = input("Enter encrypted file path: ")
        decrypt_file(path)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
