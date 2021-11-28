a = list()
a2 = list()

while True:
    try:
        line = input().split()
        if line:
            a+=line
    except:
        break

for i in range(65,91):
    sum=0
    for word in a:
        if word.startswith(chr(i)) or word.startswith(chr(i+32)):
            sum+=1
    a2.append(sum)

for i in a2:
    print(i)