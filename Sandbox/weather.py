import weather_daily
from weather_weekly import forecast as w # из модуля импортирует функцию и приваивает псевдо
print('Weather for today is', weather_daily.forecast())
print('Weather for the week is')

[print(num,key,val) for num,key,val in zip(range(1,8),w().values(),w().keys())] #Принимает словарь 