def power(n):
    if n==1:
        return True
    if n==0:
        return False
    if n%2!=0:
        return False
    return power(n/2)

a = input().split()
a2 = list()
for i in set(a):
    if not power(int(i)):
        a2.append(int(i))

for i in sorted(a2):
    print(i,end=" ")