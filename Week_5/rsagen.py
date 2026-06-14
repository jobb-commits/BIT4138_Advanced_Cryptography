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

from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

message = b"Secure Communication"

encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Encrypted Message:")
print(encrypted)

decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Decrypted Message:")
print(decrypted.decode())

print("\nSecure Message Transmission")
print("Original Message:", message.decode())
print("Encrypted Message Sent.")
print("Private Key Used for Decryption.")
print("Recovered Message:", decrypted.decode())

if decrypted == message:
    print("RSA Validation Successful!")
else:
    print("RSA Validation Failed!")