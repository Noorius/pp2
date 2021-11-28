
r,c = input().split()
r = int(r)
c = int(c)

a = []
results = []
for i in range(r):
    a.append(input().split())

for i in a:
    sum=0
    for j in i:
        sum+=int(j)
    results.append(sum)

maxi=-1000000
index=0

for i in range(len(results)):
    if results[i]>maxi and results[i]!=maxi:
        maxi=results[i]
        index=i

print(index+1)