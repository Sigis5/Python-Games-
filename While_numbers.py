print("Write down any number to add it or subtract it from the total. Type 'exit' to finish and see your final score.")
total = 0
while True:
    user_input = input("Enter a number or exit to finish: ").strip()
    if user_input.lower() == 'exit':
        break
    try:
        number = int(user_input)
        total += number          # works for both positive and negative
    except ValueError:
        print("Invalid input. Please enter a number or 'exit'.")

print(f"Your final score is: {total}")