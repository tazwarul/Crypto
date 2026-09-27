def gcd(a,b):
    while b!=0:
        temp = a
        a = b
        b= temp % b
    return a

a = int(input("Enter a: "))
b = int(input("Enter b: "))

c=gcd(a,b)

print("GCD= ",c)