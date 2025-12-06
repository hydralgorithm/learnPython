# 2D COLLECTIONS
fruits =     ["apple","orange","banana","coconut"]
vegetables = ["celery","carrots","potatoes"]
meats =      ["chicken","fish","turkey"]

groceries = [fruits,vegetables,meats]

groceries = [["apple","orange","banana","coconut"],
             ["celery","carrots","potatoes"],
             ["chicken","fish","turkey"]]

# fruits[0] = "Pineapple"

# print(groceries[0][3])
# print(groceries[1][1])

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()