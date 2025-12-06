# Dictionaries = collection of {key:value} pairs

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

# print(dir(capitals))
# print(help(capitals))

# print(capitals.get("India"))
# capitals.update({"Germany":"Berlin"})
# capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem() #Removes the latest key inserted value
# capitals.clear()

# keys = capitals.keys()
# values = capitals.values()
items = capitals.items()

# print(capitals)
# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital does not exist")

# print(keys)
# for key in capitals.keys():
#     print(key)

# print(values)
# for value in capitals.values():
#     print(value)

# print(items)
for key, value in capitals.items():
    print(f"{key} : {value}")