# LISTS, SETS AND TUPLES
# Collecetion = single "Variable" used to store multiple values
# List  = [] ordered and changeable, Duplicates ok
# Set   = {} unordered and immutable, No duplicates
# Tuple = () ordered and unchangeable, Duplicates ok

############ LIST ############

# fruits = ["apple","banana","orange","coconut"]

# print(dir(fruits)) #functions tht can be used for collections
# print(help(fruits))
# print(len(fruits))
# print("apple" in fruits)

# fruits[0] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(1,"pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("orange"))
# print(fruits.count("banana"))

# print(fruits)
# print(f"{fruits[1]}") #can use index operator to access individual elements
# print(f"{fruits[::2]}") #Can add steps
# print(f"{fruits[::-1]}") #can reverse

# for fruit in fruits:
#     print(fruit, end=" ")


############ SET ############
fruits = {"apple","banana","orange","coconut","coconut"}

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# We cant use indexing for sets because they are unordered

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop() #randomly eliminates whichever elements comes first
# fruits.clear()

# print(fruits)

############ TUPLES ############
fruits = ("apple","banana","orange","coconut","coconut")

# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("apple"))
# print(fruits.count("coconut"))

# print(fruits)