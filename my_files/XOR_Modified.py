message = input("Enter message: ")
key = int(input("Enter key (0-255): "))

encrypted = []

for char in message:
    encrypted.append(ord(char) ^ key)

print("\nEncrypted Data:")
print(encrypted)

decrypted = ""

for value in encrypted:
    decrypted += chr(value ^ key)

print("\nDecrypted Message:")
print(decrypted)