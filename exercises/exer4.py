#Hypotenuse of right angled triangle
import math
side1 = float(input("Enter dimension of side1: "))
side2 = float(input("Enter dimension of side2: "))
hypo = math.sqrt(pow(side1,2)+pow(side2,2))
print(f"Hypotenuse = {hypo}")