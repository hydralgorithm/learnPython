# Object-Oriented Programming
# from car import Car

# class Car:
#     def __init__(self, model, year, color, for_sale): #Example of constucter method and init means intialize
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

# car1 = Car("Mustang",2024,"Black",False)
# car2 = Car("Supra",2005,"Carbon Black",False)

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

# car1.describe()
# print()
# car2.describe()

#############EXAMPLE 2#############

class Student:

    class_year = 2029
    num_students = 0

    def __init__(self, name, age): #Example of constucter method and init means intialize
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Sandy", 20)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
print(student1.name)
print(student2.name)
print(student3.name)