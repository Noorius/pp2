x=input().split(",")
res=0
maxi=-10000000

for i in range(0,len(x)-1):
    if res>maxi:
        maxi=res
    res+=int(x[i])
print(maxi)
