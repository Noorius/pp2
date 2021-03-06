ft=open('read1.txt','rt').readlines()
listi=list()
for i in ft:
    listi.append(i.rstrip('\n'))
print(listi)
ft.close()