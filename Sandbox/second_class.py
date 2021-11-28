class Car():
    def exclaim(self):
        print("I am A Car!")

class Yugo(Car):
    def exclaim(self):
        print("I am A Yugo!")

print(Car().exclaim())
print(Yugo().exclaim())