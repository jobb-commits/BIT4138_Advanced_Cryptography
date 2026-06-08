import random

plaintext = "HELLO"

key = [random.randint(0, 255) for _ in plaintext]

encrypted = []

for i in range(len(plaintext)):
    encrypted.append(ord(plaintext[i]) ^ key[i])

print("Plaintext:", plaintext)
print("Key:", key)
print("Encrypted:", encrypted)

decrypted = ""

for i in range(len(encrypted)):
    decrypted += chr(encrypted[i] ^ key[i])

print("Decrypted:", decrypted)