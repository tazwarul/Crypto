  # Write a Python program to encrypt and decrypt a message using the ElGamal cryptosystem.

import random

# Input
p = int(input("Enter prime (p): "))
g = int(input("Enter primitive root (g): "))
x = int(input("Enter private key (x): "))
m = int(input("Enter message (<p): "))

# Public key
y = pow(g, x, p)
print("\nPublic Key:", (p, g, y))

# Encryption
k = random.randint(1, p-2)
c1 = pow(g, k, p)
c2 = (m * pow(y, k, p)) % p

print("\nEncrypted:", (c1, c2))

# Decryption
s = pow(c1, x, p)
m_dec = (c2 * pow(s, -1, p)) % p

print("Decrypted:", m_dec)


# Enter prime (p): 7
# Enter primitive root (g): 3
# Enter private key (x): 4
# Enter message (<p): 5

# Public Key: (7, 3, 4)

# Encrypted: (3,6)
# Decrypted: 5 


