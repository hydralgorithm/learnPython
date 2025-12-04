#Typecasting - Converting variable of one data type to other
name = "Hydrizzle"
age = 18
gpa = 8.2
is_student = True
# To detect the type of variable
print(type(gpa))

gpa = int(gpa) #Typecasting float to int
print(f"Your gpa: {gpa}")

age = float(age)
print(age)

age = str(age)
age+="1"
print(age)
print(type(age))

name = bool(name)
print(name)

# INPUTTTTT


name = input("Enter your name: ")
age = int(input("How old are you ? : "))

print(f"Hello {name}, Welcome to the team! ")
print(f"Your our youngest member of age {age}")