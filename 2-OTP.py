import random
import string

def otp(text, key, encrypt=True):
    result = ""

    for i in range(len(text)):
        t = ord(text[i]) - 65
        k = ord(key[i]) - 65

        if encrypt:
            result += chr((t + k) % 26 + 65)
        else:
            result += chr((t - k) % 26 + 65)

    return result


text = input("Enter text: ").upper()

key = ""

for i in range(len(text)):
    key += random.choice(string.ascii_uppercase)

encrypted = otp(text, key)
decrypted = otp(encrypted, key, False)

print("\nKey =", key)
print("Encrypted =", encrypted)
print("Decrypted =", decrypted)