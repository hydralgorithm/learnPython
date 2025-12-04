# STRING METHODS

name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")

# result = len(name) #Length of a string
# result = name.find(" ") #Find position of the character (0-base indexed)
# result = name.rfind("o") #Find position of the character when first encountered from end of string

# name = name.capitalize() #Capitalizes first letter of string
# name = name.upper() #Converts all characters to uppercase
name = name.lower() #Convert all char to lowercase

# result = name.isdigit() #Returns true if all characters are digits
#result = name.isalpha() #Return true if string contains only alphabetical characters

result = phone_number.count("-") #Counts how many of the specified characters are there in the string
phone_number = phone_number.replace("-"," ") #Replace characters

print(result)
print(name)
print(phone_number)

print(help(str)) #prints all the string functions