# multiple inheritance and multi-level inheritance

class Animal: #These levels of one inheriting the othe other is multi-level inheritance   
    def __init__(self,name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #Multiple inheritance, two parents
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Speedy")
fish = Fish("Jim")

fish.hunt()
fish.flee()

fish.sleep()
fish.eat()