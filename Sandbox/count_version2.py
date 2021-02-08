from collections import Counter
cnt=Counter(['a','b','a','a','a','b'])
for key,val in cnt.items():
    print(key,val) #Считает кол-во вхождений словаря