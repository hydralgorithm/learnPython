# Calculate circumference and area of a circle
import math
radius = float(input("Enter radius: "))
circum = 2*math.pi*radius
area = math.pi*pow(radius,2)
print(f"Circumference = {round(circum,2)}cm")
print(f"Area = {round(area,2)}cm²")