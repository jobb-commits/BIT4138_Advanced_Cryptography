plaintext = "NETWORK"
keyword = "KEY"

plaintext = plaintext.upper()
keyword = keyword.upper()

ciphertext = ""
key_index = 0

for char in plaintext:
    if char.isalpha():
        p = ord(char) - 65
        k = ord(keyword[key_index % len(keyword)]) - 65

        c = (p + k) % 26
        ciphertext += chr(c + 65)

        key_index += 1
    else:
        ciphertext += char

print("Plaintext:", plaintext)
print("Keyword:", keyword)
print("Ciphertext:", ciphertext)