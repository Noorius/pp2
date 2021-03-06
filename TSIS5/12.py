import math

n=int(input())
offset=0

for i in range(0,math.ceil(26/n)):
    print(''.join([chr(i) for i in range(65,91)][offset:offset+n]))
    offset+=n


