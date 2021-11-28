from collections import defaultdict
dictionary=defaultdict(int)

a=list()
while True:
    try:
        line = input().split()
        if line:
            a+=line
    except:
        break

for word in a:
    dictionary[word]+=1

for key in sorted(dictionary.keys()):
    print(key,dictionary[key])