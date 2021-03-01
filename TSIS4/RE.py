import re

with open('raw.txt','r',encoding='utf-8') as f:
    text=f.read()

companies=re.findall(r"\b[A-Za-z]{3,}\s{1}[A-Za-z]*",text)
print(companies[0],'\nBIN',re.search(r"\d{12}",text)[0])

listi=re.findall(r'.+\s\d*,\d* x [\d ]?\d*,\d*\s[\d ]?\d*,\d*',text)
listi2=[]
for m in listi:
    listi2.append(m.split("\n"))
for i in listi2:
    print(i[0],"\nCount",i[1][0],"\nUnit price",i[1].split(" x ")[1],"\nTotal price",i[2])

for i in re.findall(r'\d{2}.\d{2}.\d{4}\s\d{2}:\d{2}:\d{2}',text):
    print('Date:',i)

pattern=re.compile(r'г. \w+[-]?\w+?,\s?\w+,\s?\w+[ -]?\w+?,\s?\d+\w+?,?\s?\w+?[.\s-]?\d+?')
for i in re.findall(pattern,text):
    print(i)