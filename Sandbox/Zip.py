titles=['Creature of Habit','Crewel Fate']
plots=['A nun turns into a monster','A haunted yarn shop']
movies={}

for name, des in zip(titles,plots): #Соединяет значения из двух списков и присваивает позиционным аргументам
    movies[name]=des

print(movies)