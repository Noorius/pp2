from collections import defaultdict
dictionary=defaultdict(int)

S = list(input())
for word in S:
    dictionary[word]+=1

print(len(dictionary))
for key, val in sorted(dictionary.items()):
    print(key,val)