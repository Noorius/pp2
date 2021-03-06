import re
s=input()
k=input()
pattern=re.compile(k)
m = pattern.search(s)
if not m: print("(-1, -1)")
while m:
    print("\n(",end="")
    print(m.start(),end="")
    print(", ",end="")
    print(m.end()-1,end="")
    print(")",end="")
    m = pattern.search(s,m.start()+1)

