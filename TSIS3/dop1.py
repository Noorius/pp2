x=list(input().split(','))
target=int(input())
check=False

for i in range(len(x)-1):
    if check:
        break
    for y in range(len(x)-1):
        if int(x[i])+int(x[y])==target:
            print([i,y])
            check=True