def prime(n,m):
    if n<2:
        return False
    if n==2:
        return True
    for i in range(m,n):
        if n%i==0:
            return False
    return True
    

a = input().split()
a2 = list()

while True:
    try:
        line = input().split()
        if line:
            a+=line
    except:
        break

for i in a:
    if not prime(int(i),2) and a.count(i)>1:
        if i not in a2:
            a2.append(i)

for i in sorted(a2):
    print(i,end=" ")