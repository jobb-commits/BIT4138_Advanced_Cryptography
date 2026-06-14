from cryptography.hazmat.primitives.asymmetric import rsa

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Generate public key
public_key = private_key.public_key()

print("RSA Key Pair Generated Successfully!")
print("Private Key:", private_key)
print("Public Key:", public_key)