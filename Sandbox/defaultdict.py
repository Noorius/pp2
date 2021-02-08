from collections import defaultdict

def unknown_val():
    return 'nothing'

dictionary=defaultdict(unknown_val)
dictionary["Nur"]="Zhetessov"
x=input("Enter:\n")
print(dictionary[x]) #Заменяет несушествующие значения на "ничего"
