listi=[]
poem=''

with open('read.txt','rt',encoding='utf8') as rf:
    for line in rf:
        listi.append(line[:-1])
print(listi)