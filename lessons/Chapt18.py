# ARBITRARY ARGUMANTS
# *args - (stores in tuple) allows you to pass multiple non-key arguments
# **kwargs - (stores in dictionary) allows you to pass multiple keyword-arguments
#########################*ARGS EXAMPLE 1
def add(*nums):
    total = 0
    for num in nums:
        total+=num
    return total

print(add(1,2,5,7))
##########################*ARGS EXAMPLE 2   
def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.","Spongebob","Harold","Squarepants","III")
print()
##########################**KWARGS EXAMPLE 1
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key:10}: {value}")

print_address(street="MG Road",
              city="Bengaluru",
              state="Karnataka",
              zip="560071")
