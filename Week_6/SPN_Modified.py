# Advanced SPN Implementation

# Larger S-Box (26 letters)
S_BOX = {
    'A':'Q','B':'W','C':'E','D':'R','E':'T','F':'Y',
    'G':'U','H':'I','I':'O','J':'P','K':'A','L':'S',
    'M':'D','N':'F','O':'G','P':'H','Q':'J','R':'K',
    'S':'L','T':'Z','U':'X','V':'C','W':'V','X':'B',
    'Y':'N','Z':'M'
}


def substitute(text):
    result = ""

    for char in text:
        if char.isalpha():
            result += S_BOX[char]
        else:
            result += char

    return result


def permute(text):
    result = ""

    for i in range(0, len(text), 2):
        if i + 1 < len(text):
            result += text[i + 1] + text[i]
        else:
            result += text[i]

    return result


def add_key(text, key):
    result = ""

    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            t = ord(char) - 65
            k = ord(key[key_index % len(key)]) - 65

            result += chr((t + k) % 26 + 65)
            key_index += 1
        else:
            result += char

    return result


def spn_encrypt(plaintext, key, rounds):
    state = plaintext.upper()

    print("\nEncryption Process:")

    for r in range(rounds):
        print(f"\nRound {r + 1}")

        state = add_key(state, key)
        print("After Key Addition :", state)

        state = substitute(state)
        print("After Substitution:", state)

        state = permute(state)
        print("After Permutation :", state)

    return state


plaintext = input("Enter plaintext: ").upper()
key = input("Enter key: ").upper()
rounds = int(input("Enter number of rounds: "))

ciphertext = spn_encrypt(plaintext, key, rounds)

print("\nCiphertext:", ciphertext)