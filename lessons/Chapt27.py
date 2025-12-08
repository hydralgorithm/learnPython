# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal): #Child class
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} squeaks")

dog = Dog("Scooby")
cat = Cat("Tom")
mouse = Mouse("Jerry")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

cat.speak()
mouse.speak()