# Generate random numbers
import random

# print(dir(random))
# print(help(random))

low = 1
high = 100
options = ("Rock","Paper","Scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

# number = random.randint(1,20)
# number = random.randint(low,high)
# number = random.random() #Used for generating random floating point number
option = random.choice(options)

random.shuffle(cards)

# print(number)
# print(option)
print(cards)