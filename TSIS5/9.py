import re

with open('read_eng.txt','rt') as rf:
    text=rf.read()
    text.replace(',',' ')
print(len(text.split()))