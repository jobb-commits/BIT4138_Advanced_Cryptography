plaintext = "HELLO"
key = 121

encrypted = []

for char in plaintext:
    encrypted.append(ord(char) ^ key)

print("Encrypted:", encrypted)

decrypted = ""

for value in encrypted:
    decrypted += chr(value ^ key)

print("Decrypted:", decrypted)