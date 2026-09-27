# Write a Python program to compute the GCD of two numbers using the Extended Euclidean Algorithm.
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Compute
gcd, x, y = extended_gcd(a, b)

# Output
print("\nGCD:", gcd)
print("x:", x)
print("y:", y)

# Verification
print("\nVerification:")
print(f"{a}*({x}) + {b}*({y}) =", a*x + b*y)


# Enter first number: 48
# Enter second number: 18

