from collections import defaultdict             #Импортирует установление значений по умолчанию

with open("Text11.txt",'r') as f:               #Открывает файл с текстом, иначе не ввести
    text=f.read().split()                       #Убирает пробелы и перевод каретки

dic=defaultdict(int)                            #Устанавливает для всех ключей значение 0
listi=list() 

for i in text:
    dic[i]+=1                                   #Если есть слово в словаре, то увеличь на один
for key,val in dic.items(): 
    listi.append([val,key])                     #Кидаем в лист и меняем ключи и значения
    
listi=sorted(listi, key=lambda x: (-x[0],x[1])) #Сортируем по функции, 
                                                #где первые элементы сортировать по убыванию, 
                                                # а вторые по возрастанию

for i in listi:                                 #Получаем результат
    print(i[1])