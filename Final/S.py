n=int(input())
numbers = input().split()
maxi=-1000000
a=[]
for i in range(n):
    if int(numbers[i])>maxi:
        maxi=int(numbers[i])

a2=[]
for i in numbers:
    if int(i)==maxi:
        a2.append(1)
    else:
        a2.append(0)

for i in a2:
    print(i,end=" ")
