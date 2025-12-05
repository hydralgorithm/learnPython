# SHOPPING CART PROGRAM

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {food}: $"))
        foods.append(food)
        prices.append(price)
        total+=price

print("----- YOUR CART -----")
for food in foods:
    print(food, end = " ")
print()
print(f"Your total = ${total}")
