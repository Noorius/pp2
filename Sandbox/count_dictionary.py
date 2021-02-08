from collections import defaultdict
dictionary=defaultdict(int)
for word in ['a','b','a','a','a','b']:
    dictionary[word]+=1

for key, val in dictionary.items():
    print(key,val) #Считает кол-во вхождений словаря