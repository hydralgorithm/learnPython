# Object-Oriented Programming
from car import Car

# class Car:
#     def __init__(self, model, year, color, for_sale): #Example of constucter method and init means intialize
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

car1 = Car("Mustang",2024,"Black",False)
car2 = Car("Supra",2005,"Carbon Black",False)

# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(f"{car1.for_sale}\n")

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)

# car1.drive()
# car1.stop()
# car2.drive()
# car2.stop()

car1.describe()
print()
car2.describe()