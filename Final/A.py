import math

A = int(input())
B = int(input())

def power(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    if sum%3==0:
        return True
    else:
        return False

def four(n):
    if len(str(n))==4:
        return True
    else:
        return False

listi=[]
for i in range(A,B+1):
    #if power(i) and four(i):
    if four(pow(i,3)):
        listi.append(i)

print(listi)