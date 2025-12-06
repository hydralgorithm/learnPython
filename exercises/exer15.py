import random

# options = ("R","P","S")

options = ("rock","paper","scissors")
running = True


while running:
    print("------------------------------")
    print("Rock, Paper and Scissors game")
    print("------------------------------")
    choice = None
    computer = random.choice(options)
    while choice not in options:
        choice = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {choice}")
    print(f"Computer: {computer}")

    if choice == computer:
        print("It's a tie!")
    elif (choice=="rock" and computer=="scissors") or (choice=="paper" and computer=="rock") or (choice=="scissors" and computer=="paper"):
        print("You win!")
    else:
        print("You lose!")
    again = input("Do you wanna play again ?(y/n): ").lower()
    if not again == "y":
        running = False

print("Thanks for playing!")

# while True:
#     option = random.choice(options)
#     print("R - Rock\nP - Paper\nS - Scissor")
#     choice = input("Choose your move (R, P, S) [Q to exit]: ").upper()
#     if choice == "Q":
#         print("Successfull exit!")
#         break
#     elif (choice == "R" and option == "S") or (choice == "P" and option == "R") or (choice == "S" and option == "P"):
#         print(f"You WON! {choice} defeats {option}")
#     elif choice == option:
#         print(f"It's a TIE! {choice} balances {option}")
#     else:
#         print(f"You LOST! {option} defeats {choice}")
