# Hangman in Python
import random
from wordsList import words


hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" O ",
                   "   ",
                   "   "),
               2: (" O ",
                   " | ",
                   "   "),
               3: (" O ",
                   "/| ",
                   "   "),
               4: (" O ",
                   "/|\\",
                   "   "),
               5: (" O ",
                   "/|\\",
                   "/  "),
               6: (" O ",
                   "/|\\",
                   "/ \\"),}

def display_man(wrong_guesses):
    print("***********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    
    running_quo = True
    print("-----------------------------------")
    print("Welcome to hangman animal guesser!")
    print("-----------------------------------")
    while running_quo:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter guess letter: ").lower()
        
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid input!")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guesssed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses+=1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            running_quo = False
        elif wrong_guesses >= 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOST!")
            running_quo = False

if __name__ == '__main__':
    main()
