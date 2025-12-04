# Weight converter
weight = float(input("Enter weight: "))
unit = input("Kilograms or pounds? (K/P): ")

if unit == "K" or unit == "k":
    weight = weight * 2.205
    print(f"Weight = {round(weight,2)} Lbs")
elif unit == "P" or unit == "p":
    weight = weight/2.205
    print(f"Weight = {round(weight,2)} kgs")
else:
    print("Invalid unit!")

