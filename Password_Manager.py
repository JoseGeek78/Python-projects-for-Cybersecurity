from cryptography.fernet import Fernet
import os
import base64
import json
from getpass import getpass

# Función para generar una nueva clave maestra y guardarla en un archivo
def generate_master_key():
    key = Fernet.generate_key()
    with open("master.key", "wb") as key_file:
        key_file.write(key)

# Función para cargar la clave maestra desde un archivo
def load_master_key():
    return open("master.key", "rb").read()

# Función para cifrar una contraseña
def encrypt_password(master_key, password):
    f = Fernet(master_key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Función para descifrar una contraseña
def decrypt_password(master_key, encrypted_password):
    f = Fernet(master_key)
    decrypted_password = f.decrypt(encrypted_password).decode()
    return decrypted_password

# Función para añadir una nueva contraseña
def add_password(master_key, account, password, storage):
    encrypted_password = encrypt_password(master_key, password)
    storage[account] = encrypted_password
    save_storage(storage)

# Función para obtener una contraseña
def get_password(master_key, account, storage):
    if account in storage:
        encrypted_password = storage[account]
        return decrypt_password(master_key, encrypted_password)
    else:
        print("No se encontró la cuenta.")
        return None

# Función para guardar el almacenamiento de contraseñas en un archivo
def save_storage(storage):
    with open("passwords.json", "w") as file:
        json.dump({k: v.decode() for k, v in storage.items()}, file)

# Función para cargar el almacenamiento de contraseñas desde un archivo
def load_storage():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            storage = json.load(file)
            return {k: v.encode() for k, v in storage.items()}
    else:
        return {}

# Función principal
def main():
    if not os.path.exists("master.key"):
        print("Generando clave maestra...")
        generate_master_key()
    
    master_key = load_master_key()
    storage = load_storage()

    while True:
        print("\n1. Añadir contraseña\n2. Obtener contraseña\n3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            account = input("Nombre de la cuenta: ")
            password = getpass("Contraseña: ")
            add_password(master_key, account, password, storage)
            print("Contraseña añadida correctamente.")
        
        elif choice == "2":
            account = input("Nombre de la cuenta: ")
            password = get_password(master_key, account, storage)
            if password:
                print(f"La contraseña para {account} es: {password}")
        
        elif choice == "3":
            print("Saliendo...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
    por 