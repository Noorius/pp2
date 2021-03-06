import re
with open('read.txt','rt',encoding='utf8') as rf:
    text=rf.read()

listi=re.findall(r'[А-Яа-яёЁ]+',text)
maxi=max(listi, key=len)
print(maxi,end='')
'''
maxi=''
for i in listi:
    if len(i)>len(maxi):
        maxi=i
print(maxi)
'''