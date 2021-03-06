with open('read1.txt','rt',encoding='utf8') as rf:
    text=(''.join(rf.readlines())).split('\n')

print(sum(1 for y in text if len(y)>0))


