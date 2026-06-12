from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

with open("sample.txt", "w") as f:
    f.write("Confidential Data")

with open("sample.txt", "rb") as f:
    data = f.read()

encrypted = cipher.encrypt(data)

with open("encrypted.bin", "wb") as f:
    f.write(encrypted)

print("File encrypted successfully.")