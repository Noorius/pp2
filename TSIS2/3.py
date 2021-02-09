from collections import defaultdict
x=input().split(',')
cnt=defaultdict(int)
for num in x:
    cnt[num]+=1
sumi=0
for val in cnt.values():
    sumi+=int(val)*(int(val)-1)//2

print(sumi)