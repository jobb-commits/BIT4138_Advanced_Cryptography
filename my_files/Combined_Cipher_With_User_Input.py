def caesar_encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def vigenere_encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result


def vigenere_decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result


def main():
    print("\n=== CLASSICAL CIPHER SYSTEM ===")
    print("\nChoose Cipher:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher")

    choice = input("\nEnter choice (1 or 2): ")

    if choice == "1":
        text = input("\nEnter text: ")
        shift = int(input("Enter shift value: "))
        encrypted = caesar_encrypt(text, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        print("\n--- RESULTS ---")
        print("Original:", text.upper())
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)

    elif choice == "2":
        text = input("\nEnter text: ")
        key = input("Enter keyword: ")
        encrypted = vigenere_encrypt(text, key)
        decrypted = vigenere_decrypt(encrypted, key)
        print("\n--- RESULTS ---")
        print("Original:", text.upper())
        print("Key:", key.upper())
        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)

    else:
        print("Invalid choice!")


main()