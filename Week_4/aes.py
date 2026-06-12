from cryptography.fernet import Fernet
key = Fernet.generate_key()

# Create AES object
cipher = Fernet(key)

# Message to encrypt
message = b"Hello AES"

# Encrypt
encrypted = cipher.encrypt(message)

print("Encrypted:", encrypted)

