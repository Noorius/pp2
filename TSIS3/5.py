from collections import deque

def move(k):
    while k!=0:
        if(k>0):
            x.appendleft(x.pop())
            k-=1
        else:
            x.append(x.popleft())
            k+=1

x=deque(input().split())
k=int(input())
move(k)
print(x)