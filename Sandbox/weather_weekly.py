def forecast():
    from random import choice
    possibilities=['snow','rain','sleet','fog','wind','cloudy','cold','hot']
    weekly={}
    for i in range(30):
        weekly[choice(range(-30,30,1))]=choice(possibilities)
    return weekly #Возвращает словарь из случайных ключей из в районе чисел и случ. значений из списка