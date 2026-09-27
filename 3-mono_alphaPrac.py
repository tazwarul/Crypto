def mono (text, key, encrypt= True):
    result = ""

    for i in range(len(text)):
        if text[i].isupper():
            if encrypt:
                result+=key[ord(text[i])-65]
            else:
                result+=chr(key.index(text[i])+65)
        else: 
            result += text[i]
    return result

text = input("Enter text: ").upper()
key = input("Enter 26-letter key: ").upper()

encrypted = mono(text, key)
decrypted = mono(encrypted, key, False)

print("Encrypted =", encrypted)
print("Decrypted =", decrypted)
        