# read only --> you can't set the value. value can't be change
# getter --> get a value of a property through a method. most of the time, you will get a value of a prive attribute.
# setter --> set a value of a property through a method. Most of the time , you will set a value of a private property. 

class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money 

    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age
    
    # getter
    @property
    def salary(self):
        return self.__money
    
    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return "salary can't be negative"
        self.__money += value

samsu = User('kopa', 25, 5000)

# print(samsu.__money)
# print(samsu.age())
print(samsu.age)
# print(samsu.salary())
print(samsu.salary)
samsu.salary = 12000
print(samsu.salary)