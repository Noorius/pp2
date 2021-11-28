import math
sum1= 0
sum2 = 0
for j in range(2):
    sum2=sum1
    for i in range(2,-1,-1):
        sum1 += int(input()) * pow(60,i)
    sum1 -= sum2
print(sum1-sum2)