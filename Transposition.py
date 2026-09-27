import math

print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter Choice (1/2): ")

key = int(input("Enter Key (number of columns): "))

if choice == "1":
    text = input("Enter Plain Text: ").replace(" ", "").upper()

    while len(text) % key != 0:
        text += "X"

    rows = len(text) // key

    matrix = []
    index = 0

    for i in range(rows):
        row = []
        for j in range(key):
            row.append(text[index])
            index += 1
        matrix.append(row)

    cipher = ""

    for j in range(key):
        for i in range(rows):
            cipher += matrix[i][j]

    print("Encrypted Text:", cipher)

elif choice == "2":
    cipher = input("Enter Cipher Text: ").replace(" ", "").upper()

    rows = math.ceil(len(cipher) / key)

    matrix = [["" for _ in range(key)] for _ in range(rows)]

    index = 0

    for j in range(key):
        for i in range(rows):
            if index < len(cipher):
                matrix[i][j] = cipher[index]
                index += 1

    plain = ""

    for i in range(rows):
        for j in range(key):
            plain += matrix[i][j]

    print("Decrypted Text:", plain.rstrip("X"))

else:
    print("Invalid Choice")