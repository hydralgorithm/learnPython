# Iterables

#########EXAMPLE 1##########
numbers = [1,2,3,4,5]

for num in numbers:
    print(num,end="-")
print()
#########EXAMPLE 2##########
fruits = {"apple","orange","banana","coconut"}

for fruit in fruits:
    print(fruit)
#########EXAMPLE 3##########
name = "Bro code"

for character in name:
    print(character,end=" ")
print()
#########EXAMPLE 4##########
my_dictionary = {"A":1,"B":2,"C":3}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")
    