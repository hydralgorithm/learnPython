# Functions 

# EXAMPLE 1
# def happy_birthday(name,age):
#     print(f"Happy Birthday to you {name}!")
#     print(f"You are {age} years old!")
#     print("Happy Birthday to you!")
#     print()

# happy_birthday("Bro",20)
# happy_birthday("Steve",18)
# happy_birthday("Rob",7)

# EXAMPLE 2
# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due : {due_date}")

# display_invoice("Hydralgorithm",100.01,"01/02")    

# RETURN

# EXAMPLE 1
def add(a,b):
    sum = a + b
    return sum

x = 5
y = 6
sol = add(x,y)
print(add(x,y))
print(sol)

# EXAMPLE 2
def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first+" "+last

full_name = create_name("john","baller")
print(full_name)