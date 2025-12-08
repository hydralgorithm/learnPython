# Class methods

class Student:

    count = 0 
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

# Instance method because (self) is first parameter
    def get_info(self):
        return f"{self.name} - {self.gpa}"
    
# Class method we use (cls) as first parameter, we declare class method using class method decorator @
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa of students: {cls.total_gpa/cls.count:.2f}"

Stud1 = Student("John", 8.3)
Stud2 = Student("Pery", 7.6)
Stud3 = Student("Ron", 9.4) 
    
print(Student.get_count())
print(Student.get_avg_gpa())