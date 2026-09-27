def caesar(text, key):
    result=""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch)-65 +key) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch)-97 + key) % 26 +97)
        else:
            result += ch
    return result
text = input("Enter Text: ")
key= int(input("Enter Key"))

en = caesar(text,key)
print("\nEncryted text: ",en)

print("\nBrute Force result: ")
for key in range(26):
    de= caesar(en,-key)
    print("Key", key, ":", de)