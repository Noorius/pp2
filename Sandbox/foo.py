class Person:
    def __init__(self,name,age='None'):
        self.__name=name
        self.__age=age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @property
    def age(self):
        return self.__age 
    @age.setter
    def age(self,age):
        self.__age=age

    def hi(self):
        print('Name: ',self.__name,'Age: ',self.__age,end=' ')

class Employee(Person):
    def __init__(self,name,age,company='Unemployed'):
        Person.__init__(self,name,age)
        self.__company=company
    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self,company):
        self.__company=company
    def hi(self):
        Person.hi(self)
        print('Company:',self.company)
    def __str__(self):
        return "Name: {}, Age: {}".format(self.name,self.age)

worker=Employee('Tom','21','Google')
#print(worker.name,worker.age)
#worker.company('Microsoft')
#print(worker.hi())
print(worker)
