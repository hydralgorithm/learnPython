#Validate user input
name = input("Enter username: ")
result = name.isalpha()
count = len(name)
finder = name.find(" ") 
if not result:
    print("Should not contain digits!")
elif count>12 or count<1 :
    print("Exceeded char limit!")
elif not finder == -1:
    print("No spaces!")
else:
    print("Valid username!")