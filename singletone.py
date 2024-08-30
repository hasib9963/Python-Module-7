# single tone --> one single instance/object
# if you want a new instance/object, you will get the old one (already created) instance/object

class Singletone:
    __instance = None
    def __init__(self) -> None:
        if Singletone.__instance is None:
          Singletone.__instance = self 
        else:
           raise Exception('This is singletone. Alredy have an instance/object, use that one by calling get_instance methiod')
        
    @staticmethod
    def get_instance():
       if Singletone.__instance is None:
          Singletone()
       return Singletone.__instance

first = Singletone.get_instance()
second = Singletone.get_instance()
third = Singletone.get_instance()
print(first)
print(second)
print(third)

# last = Singletone()

# book --> Design pattern --> eich gamma
# book --> code complete --> 2nd edition