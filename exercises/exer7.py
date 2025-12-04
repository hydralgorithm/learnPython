# Temperature converter
unit = input("Is this temp in celcius or fahrenheit? (C/F): ")
temp = float(input("Enter temperature: "))
if unit=="F" or unit=="f":
    temp=(5*(temp-32))/9
    unit = "C"
    print(f"Temperature = {round(temp,2)}°{unit}")
elif unit=="C" or unit=="c":
    temp= (9*temp)/5 + 32
    unit="F"
    print(f"Temperature = {round(temp,2)}°{unit}")
else:
    print("Invalid unit!")