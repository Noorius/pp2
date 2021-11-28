a = {}
while True:
    try:
        line = input().split()
        if int(a[line[0]])<int(line[1]):
            a[line[0]]=line[1]
    except:
        break
print(a)