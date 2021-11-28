w1=input()
w2=input()
if len(w1)!=len(w2):
    print('NO')
    quit()

dic1 = {}
dic2 = {}
for i in w1:
    if i not in dic1.keys():
        dic1[i]=0
    else:
        dic1[i]+=1
for i in w2:
    if i not in dic2.keys():
        dic2[i]=0
    else:
        dic2[i]+=1

if set(dic1.keys())!=set(dic2.keys()):
    print("NO")
    quit()

for key in dic1.keys():
    if key in dic2.keys():
        if dic1[key]!=dic2[key]:
            print("NO")
            quit()
    else:
        print("NO")
        quit()

print("YES")