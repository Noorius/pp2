x=set(input().split())
y=list(input().split())
sum=0
for i in x:
    sum+=y.count(i)
print(sum)

