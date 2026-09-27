def transposition(text, key):
    result = ""

    text = text.replace(" ", "")

    while len(text) % len(key) != 0:
        text += "X"

    cols = len(key)
    rows = len(text) // cols

    for col in sorted(range(cols), key=lambda x: key[x]):
        for row in range(rows):
            result += text[row * cols + col]

    return result


text = input("Enter message: ").upper()
key1 = input("Enter first key: ").upper()
key2 = input("Enter second key: ").upper()

first = transposition(text, key1)
encrypted = transposition(first, key2)

print("Plaintext =", text)
print("First Encryption =", first)
print("Double Encryption =", encrypted)