n, m = map(int, input().split())
Bo=set()
An=set()
for i in range(n):
    x=int(input())
    Bo.add(x)
for i in range(m):
    x=int(input())
    An.add(x)
a=Bo.intersection(An)
print(len(a))
l=sorted(list(a))
for i in l:
    print(i,end=" ")
print()

a1=sorted(Bo.difference(a))
print(len(a1))
for i in a1:
    print(i,end=" ")
print()

a1=sorted(An.difference(a))
print(len(a1))
for i in a1:
    print(i,end=" ")
print()
