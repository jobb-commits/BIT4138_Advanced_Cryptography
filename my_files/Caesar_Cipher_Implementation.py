text = "SECURITY"
shift = 4

result = ""

for char in text:
    if char.isalpha():
        result += chr((ord(char) - 65 + shift) % 26 + 65)

print("Encrypted:", result)