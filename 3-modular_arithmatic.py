# Write a Python program to perform modular arithmetic operations using a primitive root.

# Input
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("\n--- Modular Arithmetic Operations ---")

# Addition
print("Addition:", (a + b) % p)

# Subtraction
print("Subtraction:", (a - b) % p)

# Multiplication
print("Multiplication:", (a * b) % p)

# Exponentiation using primitive root
print("g^a mod p:", pow(g, a, p))

# Verify primitive root powers
print("\n--- Powers of g mod p ---")
for i in range(1, p):
    print(f"{g}^{i} mod {p} =", pow(g, i, p))
    
    


# Enter prime number (p): 7
# Enter primitive root (g): 3
# Enter first number (a): 2
# Enter second number (b): 4