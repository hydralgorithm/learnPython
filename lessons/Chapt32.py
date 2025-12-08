# Static Methods

class Employee:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def get_info(self): #instance method
        return (f"{self.name} = {self.position}")

    @staticmethod
    def is_valid_position(position):#Static method belongs to class, not any object created from the class
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

employee1 = Employee("Eugene","Cashier") #For instance method
employee2 = Employee("Aladin","Manager")
employee1 = Employee("Sandy","Cook")
print(employee1.get_info())

print(Employee.is_valid_position("Cook")) #For static method

