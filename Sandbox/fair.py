key=input("Enter a key word: \n")
pt=input("Enter a plaintext: \n")
listi=list()
main=list()

for j in range(65,91):
    for i in key:
        if i not in listi and i!='J':
            listi.append(i)
    if chr(j) not in listi and j!=74:
        listi.append(chr(j))

k=1
temp=list()
for i in listi:
    temp.append(i)
    if k%5==0:
        main.append(temp)
        temp=list()
    k+=1

for i, j in pt:
    print(i,j)
print(main)