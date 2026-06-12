message = "HELLO"
keystream = [14, 65, 78, 23, 56]

encrypted = []

for i in range(len(message)):
    encrypted.append(ord(message[i]) ^ keystream[i])

print("Encrypted:", encrypted)

decrypted = ""

for i in range(len(encrypted)):
    decrypted += chr(encrypted[i] ^ keystream[i])

print("Decrypted:", decrypted)