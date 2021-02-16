x=list(input().split())
for i in x:
    if i=='0':
        x.remove(i)
        x.append("0")
print(x)