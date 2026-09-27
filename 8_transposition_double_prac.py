def transposition (text,key):
    result = ""

    text = text.replace(" ","")

    while len(text) % len(key) !=0:
        text += "X"

    cols = len (key)
    rows= len (text) // cols

    for col in sorted (range(cols), key=lambda x: key [x]):
        for row in range (rows):
            result += text[row * cols +col]
    return result

text = input ("Enter msg= ").upper()
key1 = (input("Key 1 : ")).upper()
key2 = (input("Key 2 : ")).upper()

first = transposition(text,key1)
second= transposition(first, key2)

print("Plaintext =", text)
print("First Encryption =", first)
print("Double Encryption =", second)