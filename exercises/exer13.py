# Concession Stand Program
menu = {"pizza":3.00,
        "nachos":4.50,
        "popcorn":3.75,
        "fries":1.25,
        "chips":2.00,
        "soda":3.50,
        "juice":3.00}

cart = []
total = 0
print("---------MENU---------")
for food, price in menu.items():
    print(f"{food:10} -  ${price:.2f}")
print("----------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)

print("-------------------------")
print("         BILLING         ")
print("-------------------------")
for snack in cart:
    print(f"{snack:10}: ${menu.get(snack):.2f}")

print("-------------------------")
print(f"Total = ${total}")
