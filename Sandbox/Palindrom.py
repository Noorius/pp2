def palindrom(word):
    from collections import deque
    dq=deque(word)
    while len(dq)>1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrom(input())) #Создаем дэк и сравниваем результаты функц. pop() пока длина больше 1
