# IF ELSE STATEMENTS
age = int(input("Enter your age: "))

if age>=90:
    print("Your too old to drive!")
elif age>=18:
    print("Eligible for license.")
elif age<0:
    print("You don't exist yet!")
else:
    print("Not Eligible!")

response = input("Would you like some food? (Y/N): ")
if response == "Y" or response == "y":
    print("Have some food!")
elif response =="N" or response == "n":
    print("Too bad, have some food next time.")
else:
    print("Choose one option timber legs!")

for_sale = False
if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")