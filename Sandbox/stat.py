x=list(input().split(', '))
x = sorted(x, key=lambda x: int(x))

Q1=(len(x)+1)/4
Q1=int(x[int(Q1)-1])+Q1%1*(int(x[int(Q1)])-int(x[int(Q1)-1]))
Q3=(3*(len(x)+1))/4
Q3=int(x[int(Q3)-1])+Q3%1*(int(x[int(Q3)])-int(x[int(Q3)-1]))
print('The interquartile range is', Q3-Q1)

