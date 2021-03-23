answer=bool(int(input("0 - decrypt \n1 - crypt\n")))
secret=input("Enter a text: ")
key=input("Enter a key: ")
i=len(key)
keystream=""

for _ in secret:
    if i==len(key):
        i=0
    keystream+=key[i]
    i+=1

for i, j in zip(secret,keystream):
    if answer:
        new=ord(i)+ord(j)-65
        if new>90:
            new -= 26
    else:
        new=ord(i)-ord(j)+65
        if new<65:
            new += 26
    crypt+=chr(new)
print(crypt)
        
