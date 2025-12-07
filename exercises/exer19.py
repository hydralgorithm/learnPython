# Slot Machine
import random

def spin_row():
    symbols = ['🍉','🍒','🍋 ','🔔','⭐']
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print("~~~~~~~~~~~~~~~")
    print(" | ".join(row))
    print("~~~~~~~~~~~~~~~")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        won = bet*10
        print(f"You won ${won}")
        return won
    else:
        return 0
def main():
    balance = 100

    print("--------------------------")
    print("Welcome to Slot Clanker !")
    print("Symbols: 🍉 🍒 🍋 🔔 ⭐")
    print("--------------------------")

    while balance>0:
        print(f"Current balance: ${balance}")
        
        bet = input("Enter your bet amount (q to exit): ")
        if bet.lower() == "q":
            break
        if not bet.isdigit():
            print("Invalid bet!")
            continue
        bet = int(bet)
        if bet > balance:
            print("Bet amount can't cross balance!")
            continue
        elif bet <= 0:
            print("Bet something boy!")
            continue
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)
        balance += get_payout(row,bet)

    if balance == 0:
        print("Looks like your broke! Have a good day!")
    elif balance > 100:
        print("Congrats on turning in profit! Have a bad day!")
    else:
        print("Atleast you have more than a penny !")


if __name__ == '__main__':
    main()
