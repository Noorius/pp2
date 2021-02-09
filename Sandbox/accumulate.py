import itertools

for word in itertools.accumulate([1,2,3,4],lambda arg1,arg2: arg1*arg2/2):
    print(word)