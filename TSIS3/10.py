d={}

for i in range(int(input())):
    x, y = input().split()
    d.update({x:y})

word=input()

for key,val in d.items(): 
    if key==word:
        print(val)
    elif val ==word:
        print(key)