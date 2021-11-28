n = int(input())
m = int(input())
maxi = -10000000
k,l = 0, 0

'''
for i in range(n):
    for j in range(m):
        a = int(input())
        if a>maxi:
            k, l = i, j
            maxi=a
print(k,l)
'''

a = [[int(j) for j in input().split()] for i in range(n)]

