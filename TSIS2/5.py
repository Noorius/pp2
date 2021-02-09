x=input()
sumi = 0
pr = 1
for i in x:
    sumi+=int(i)
    pr*=int(i)
print(pr-sumi)