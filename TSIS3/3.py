x=list(input().split())
i,j=[0,len(x)-1]
while i<j:
    t=x[i]
    x[i]=x[j]
    x[j]=t
    i+=1
    j-=1

print(x)