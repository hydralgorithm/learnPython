# Format specifiers
# .(number)f = round to that many decimal points
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator 
 
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# print(f"Price 1 is ${price1:.1f}")
# print(f"Price 2 is ${price2:.1f}")
# print(f"Price 3 is ${price3:.1f}")

# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")

# print(f"Price 3 is ${price3:010}")


# print(f"Price 1 is ${price1:<10}")
# print(f"Price 2 is ${price2:<10}")
# print(f"Price 3 is ${price3:<10}")


# print(f"Price 1 is ${price1:>10}")
# print(f"Price 2 is ${price2:>10}")
# print(f"Price 3 is ${price3:>10}")


# print(f"Price 1 is ${price1:^10}")
# print(f"Price 2 is ${price2:^10}")
# print(f"Price 3 is ${price3:^10}")


# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")


# print(f"Price 1 is ${price1: }")
# print(f"Price 2 is ${price2: }")
# print(f"Price 3 is ${price3: }")


# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")

#You can also combine different specifiers

print(f"Price 1 is ${price1:>10,.2f}")
print(f"Price 2 is ${price2:>10,.2f}")
print(f"Price 3 is ${price3:>10,.2f}")