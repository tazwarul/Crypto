def hill (text, key, encrypt= True):
    result = ""

    for i in range(0,len(text),2):
        a= ord(text[i])-65
        b= ord (text[i+1])-65

        if encrypt:
            x=(key[0][0] * a + key[0][1]*b ) % 26
            y=(key[1][0] *a + key[1][1]) % 26
        else:
            det = (key[0][0]*key[0][1]-key[1][0]*key[1][1]) % 26

            inv_det = pow (det, -1, 26)
            x= (inv_det * (key[1][1] * a + key[0][1]*b)) % 26
            y= (inv_det * (key[1][0] * a + key[0][0]*b)) % 26 

        result += chr(x+65)
        result += chr(y+65)
    return result


text = input ("Enter text : ").upper()

if len(text) % 2 !=0:
    text +="X"

print("Enter 2*2 mattrix: ")

a= int(input("Enter a: "))
b= int(input("Enter b: "))
c= int(input("Enter c: "))
d= int(input("Enter d: "))

key = [[a,b],[c,d]]

en = hill(text, key)
de = hill(en,key, False)

print("\nMattrix: ")
print(key)

print("Encrypted: ",en)
print("Decripted: ",de)