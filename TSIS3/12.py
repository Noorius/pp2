from collections import defaultdict
dic=defaultdict(int)

for i in range(int(input())-1):
    x,y=input().split()
    dic[x]+=1+dic[y]

for key,val in sorted(dic.items()):
    print(key,val)

