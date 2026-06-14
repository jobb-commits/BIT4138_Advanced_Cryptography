# Basic SPN Implementation
s_box = {
    'A': 'Q', 'B': 'W', 'C': 'E', 'D': 'R',
    'E': 'T', 'F': 'Y', 'G': 'U', 'H': 'I',
    'I': 'O', 'J': 'P', 'K': 'A', 'L': 'S',
    'M': 'D', 'N': 'F', 'O': 'G', 'P': 'H',
    'Q': 'J', 'R': 'K', 'S': 'L', 'T': 'Z',
    'U': 'X', 'V': 'C', 'W': 'V', 'X': 'B',
    'Y': 'N', 'Z': 'M'
}

plaintext = input("Enter plaintext: ").upper()

# Step 1: Substitution
substituted = ""

for char in plaintext:
    if char.isalpha():
        substituted += s_box[char]
    else:
        substituted += char

# Step 2: Permutation
ciphertext = ""

for i in range(0, len(substituted), 2):
    if i + 1 < len(substituted):
        ciphertext += substituted[i + 1] + substituted[i]
    else:
        ciphertext += substituted[i]

# Display results
print("\nPlaintext:", plaintext)
print("After Substitution:", substituted)
print("Ciphertext:", ciphertext)