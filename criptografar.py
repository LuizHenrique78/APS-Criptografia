from cryptography.fernet import Fernet


key = Fernet.generate_key()
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)
with open('arquivo.txt', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open('arquivo.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)