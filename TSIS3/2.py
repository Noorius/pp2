x=list(input().split())
max=1001
for i in x: 
    if int(i)>0 and int(i)<int(max): 
        max=i
print(max)