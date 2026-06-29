# Diffie-Hellman Key Exchange

print("Diffie-Hellman Key Exchange")

#Public values
p = int(input("Enter a prime number (p): "))
g = int(input("Enter a generator (g): "))

#Private keys
alice_private = int(input("\nAlice's private key: "))
bob_private = int(input("Bob's private key: "))

# Generate public keys
alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("\nPublic Keys")
print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)

#Compute shared secrets
alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)

#Display results
print("\nShared Secret")
print("Alice's Secret:", alice_secret)
print("Bob's Secret:", bob_secret)

# Verify
if alice_secret == bob_secret:
    print("\nSuccess! Both users generated the same secret key.")
else:
    print("\nError! Shared secrets do not match.")