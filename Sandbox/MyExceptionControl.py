class OopsException(Exception): #Создает исключение, позволяет системе вывести ошибку самостоятельно
    pass

listi=[1,2,3]
position=input('Enter position\n')
try:
    print(listi[int(position)]) 
except:
    raise(OopsException('Caught an oops'))