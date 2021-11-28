import math

pairs =[(x,y)
 for x in range(10)
 for y in range(x+1,10)]

listi = sorted(pairs, key=lambda z: math.sqrt(z[0]**2+z[1]**2), reverse=True)

print(listi)