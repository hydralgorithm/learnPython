# Number guessing game
import random
answer = random.randint(1,100)
trial = 0

while True:
    guess = input("Enter a number between 1 and 100: ")
    
    if guess.isdigit():
        trial += 1
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Number is out of range!")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of trials: {trial}")
            break 
    else:
        print("Invalid guess!")