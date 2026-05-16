import random
#Game
def game():
    secret = random.randint(1, 100)
    attempts = 5

    while attempts > 0:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("That's not a number! You lost an attempt for being silly.")
            attempts -= 1
            continue
        if guess == secret:
            print("Congratulations! You guessed the number.")
            break
        else:
            distance = abs(guess - secret)
            print(f"Wrong guess! You are {distance} units away from the secret number.")
        attempts -= 1
        if attempts == 0:
            print("Sorry, you've used all your attempts. The number was:", secret)

print("Welcome to the Number Guesser Game!")

print("I have selected a secret number between 1 and 100. You have 5 attempts to guess it.")

while True:
    start = input("Enter W to play, anything else to exit: ")
    if start == "W":
        game()
    else:
        break
print("Thank you for playing! Goodbye!")
