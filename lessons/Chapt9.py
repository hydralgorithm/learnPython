# For loops (inclusive start,exclusive end, steps)

# EXAMPLE 1
# for x in range(1,11):
    # print(x)

# EXAMPLE 2
# for x in reversed(range(1,11)):
#     print(x)
# print("HAPPY NEW YEAR")

# EXAMPLE 3
# for x in range(1,11,3):
#     print(x)

# EXAMPLE 4
# credit_number = "1234-5678-9012-3456"
# for x in credit_number:
#     print(x)

# EXAMPLE 5
for x in range(1,21):
    if x == 13:
        continue
    elif x == 19:
        break
    else:
        print(x)