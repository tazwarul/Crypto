# Write a Python program to simulate the Diffie-Hellman key exchange.

# Input
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter Alice private key: "))
b = int(input("Enter Bob private key: "))

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

print("\nPublic Values:")
print("Alice sends:", A)
print("Bob sends:", B)

# Shared secret
key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("\nShared Key (Alice):", key1)
print("Shared Key (Bob):", key2)





# Enter prime number (p)s: 7
# Enter primitive root (g): 3
# Enter Alice private key: 4
# Enter Bob private key: 5

# Public Values:
# Alice sends: 4
# Bob sends: 5

# Shared Key (Alice): 2
# Shared Key (Bob): 2