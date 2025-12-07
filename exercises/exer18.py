# PYTHON BANKING PROGRAM

def show_bal(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    if amount < 0:
        print("That's not a valid amount: ")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount you want to withdraw: "))
    if amount > balance:
        print("You don't have that kinda money, brokie!")
        return 0
    elif amount < 0:
        print("I see what u tryin boy")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("#####Banking Program#####")
        print("1.Show Balance\n2.Deposit\n3.Withdraw\n4.Exit")

        choice = input("Enter your choice (1-4): ")

        match choice:
            case "1":
                show_bal(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("Invalid choice. Please try again.")
        print()
    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()