class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def eat(self):
     print('Rice, meat, Polao, Biriyani') 

    def exercise(self):
        raise NotImplementedError

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team 
        super().__init__(name, age, height, weight)

    # Override
    def eat(self):
      print('vegitables') 

    def exercise(self):
       print('Gym a poisa diya Gham jorai')

    # + sign overload
    def __add__(self, other):
       return self.age + other.age
    
    # * sign overload
    def __mul__(self, other):
       return self.weight * other.weight 
    
    # lenth overload
    def __len__(self):
       return self.weight
    
    # > operator overload
    def __gt__(self, other):
       return self.age > other.age


sakib = Cricketer("Sakib AL Hasan", 36, 5.10, 75, 'Bangladesh')
mushi = Cricketer('Mushfiqur Rahim', 35, 5.2, 65, 'Bangladesh') 
# sakib.eat()
# sakib.exercise()

# plus sign overload korteci
print(45 + 63)
print('sakib' + 'rakib')
print([12, 98] + [13, 102])
print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib > mushi)