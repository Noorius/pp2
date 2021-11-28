

def prime(n):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

A, B = input().split()
a = list()
for i in range(int(A),int(B)+1):
    if prime(i):
        a.append(i)

for i in a[::-1]:
    print(i,end=" ")