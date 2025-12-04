# # Calculate rectangle area
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print(f"Area of rectangle is {area}cm²")

# Shopping cart program
item = input("Enter your item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price of item: "))
total = price*float(quantity)
print(f"Your total for {quantity} {item}'s is ${total}")