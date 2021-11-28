def palindrom(word):
    from collections import deque
    dq=deque(word)
    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return False
    return True

listi = set(input().split())
listi2 = []
for i in listi:
    if not palindrom(i):
        listi2.append(i)

for i in sorted(listi2):
    print(i)