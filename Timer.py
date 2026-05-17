import time

# Get input from user
task_name = input("Task name: ")

while True:
    duration_input = input("Duration (minutes): ")
    try:
        duration = int(duration_input)
        if duration <= 0:
            print("Please enter a positive number for duration.")
            continue
        break
    except ValueError:
        print("Invalid input: please enter a number for duration.")

# Convert minutes to seconds
total_seconds = duration * 60

print(f"\nStarting: {task_name}")
print(f"Duration: {duration} minutes\n")

# Countdown loop
while total_seconds > 0:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    
    # Display time remaining
    print(f"{minutes}:{seconds:02d} remaining...", end="\r")
    
    # Wait 1 second
    time.sleep(1)
    
    # Decrease counter
    total_seconds -= 1

print(f"\nTime's up! {task_name} session complete!")

        