n=int(input())
poem=''

with open('read.txt','rt',encoding='utf8') as rf:
    ft=open('write2.txt','wt',encoding='utf8')
    ft.write(''.join(reversed(rf.read())))
    ft.close()

with open('write2.txt','rt',encoding='utf8') as rt:
    while n> 0:
        print(rt.readline()[::-1],end='')
        n-=1

    