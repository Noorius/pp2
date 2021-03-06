import random
import glob
listi=glob.glob('*.txt')

ft1=open('read_eng.txt','rt')
ft2=open("read.txt",'rt',encoding='utf8')
ft3=open('read1.txt','rt')

list1=random.sample(ft1.read().replace(' ',''),10)
list2=random.sample(ft2.read().replace(' ',''),10)
list3=random.sample(ft3.read().replace(' ',''),10)

print(random.sample(list1+list2+list3,10))

char=list()
for i in listi:
    with open(i,'rt',encoding='utf8') as f:
        char.append(f.read())
print(char)