import os
import shutil

print(os.path.getsize("read1.txt"))
print(os.stat('read1.txt').st_size)

listi=['apple','banana','orange']
ft=open("write3.txt",'wt')
ft1=open('read1.txt','rt')

for i in listi:
    ft.write(i+'\n')
ft.write(ft1.read())
shutil.copyfile('read1.txt','write3.txt')

ft.close()
ft1.close()