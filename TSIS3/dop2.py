from collections import deque

dic={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

x=deque(input())
sum=0

for i in range(len(x)):
    if len(x)==1:
        sum+=dic[x[0]]
        break
    elif dic[x[0]]>=dic[x[1]]:
        sum+=dic[x.popleft()]
    else:
        sum-=dic[x.popleft()]
    
print(sum)