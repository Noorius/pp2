import itertools
#a,b,c=input().split()
#print(max(int(a),int(b),int(c)))

listi=[1,2,3,3,3,6,6,8,8,1,2,2,2,2,2,2,2]
x = itertools.accumulate(listi,lambda y1,y2: y1*y2)
#print(list(x)[-1])

def factorial(num: int):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)

#a=int(input())
#start,end=input().split()
#print('YES' if a in range(int(start),int(end)) else "NO")

def lowup(word: str):
    up = sum(1 for y in word if 65<=ord(y)<=90)
    low = sum(1 for y in word if 97<=ord(y)<=122)
    print(f'Low {low}, Up: {up}')

listi2=[]
listi2 = [y for y in listi if y not in listi2]
print(listi2)