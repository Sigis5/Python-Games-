import time
import sys

#Bank
def bank():
    balance = 0    
    while True: 
        choise = input("Welcome to the bank, press A to add or W to withdraw money from your bank account: ").lower().strip()
        if choise in ("a", "w"):
            try:
                if choise == "a":
                    plus = int(input("Choose how much money do you want to add to your bank account: "))
                    balance += plus
                    print(f"This is your current bank balance: {balance}")
                elif choise == "w":
                    minus = int(input("Choose how much money do you want to withdraw from your bank account: "))
                    if minus > balance:
                        print("You don't have enough money in your balance")
                    else:
                        balance -= minus
                        print(f"This is your current bank balance: {balance}")
            except ValueError:
                print("Wrong input - please enter a number")
                continue
            
            another = input("Do another transaction? (y/n): ").lower().strip()
            if another != "y":
                print("Exiting bank... Goodbye!")
                time.sleep(3)
                sys.exit()
                break
        else:
            print("Wrong input")
            
            
def game():
    while True:
        a = input("Press a to continue: ").lower()
        if a == "a":
            bank()
            break
        else:
            print("Wrong input")
game()
