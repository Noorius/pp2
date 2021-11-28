'''
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
s = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
print(s)
'''
n = 3
m = 4
a = [0] * n
for i in range(n):
    a[i] = [0] * m

n = 3
m = 4
a = []
for i in range(n):
    a.append([0] * m)

n = 3
m = 4
a = [[0] * m for i in range(n)]
