answer=bool(int(input("0 - crypt\n1 - decrypt\n")))
pt=input('Enter a text\n')
key=input("Enter a key\n") or 3

ct=""
for i in pt:
    if answer:
        if ord(i)-int(key)<65:
            ct+=chr((26-int(key))+ord(i))
        ct+=chr(ord(i)-int(key))
    else:
        if ord(i)-int(key)>90:
            ct+=chr(ord(i)-(26-int(key)))
        ct+=chr(ord(i)+int(key))
print(ct)