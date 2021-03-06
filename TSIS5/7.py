import random
import os

ft1=open('read.txt','rt',encoding='utf8')
ft2=open('read_eng.txt','rt')
#for line1, line2 in zip(ft1,ft2):
    #print(line1+line2,end='')

print(ft1.closed)
print(random.choice(ft1.readlines()),end="")
ft1.close()
ft2.close()
print(ft1.closed,end="")