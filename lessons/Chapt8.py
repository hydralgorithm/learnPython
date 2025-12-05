# While loops
# EXAMPLE 1
# name = input("Enter your name: ")

# while name=="":
#     print("You did not enter your name")
#     name = input("Enter your name: ")

# print(f"Hello, {name}")

# EXAMPLE 2
# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative!")
#     age = int(input("Enter age: "))

# print(f"You are {age} years old.")

# EXAMPLE 3
# food = input("Enter a food you like (q to exit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (q to exit): ")
# print("Bye")


# EXAMPLE 4
num = int(input("Input a number between 1-10: "))

while num<1 or num>10:
    print("Number out of bonds! Enter again!")
    num = int(input("Input a number between 1-10: "))
print(f"Your lucky number is {num}!")