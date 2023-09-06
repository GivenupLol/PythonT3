# Import the 'randint' function from the 'random' module
from random import randint

# Prompt the user for the number of digits in the PIN (between 4 and 16 inclusive)
while True:
    try:
        num_digits = int(input("Enter the number of digits in the PIN (4-16): "))
        if 4 <= num_digits <= 16:
            break
        else:
            print("Please enter a valid number of digits between 4 and 16.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Prompt the user for the test range
while True:
    try:
        start_range = int(input("Enter the start of the test range: "))
        end_range = int(input("Enter the end of the test range: "))
        if start_range < end_range:
            break
        else:
            print("Invalid range. End range must be greater than start range.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Generate a random PIN with the specified number of digits
min_pin = 10 ** (num_digits - 1)
max_pin = (10 ** num_digits) - 1
pin = randint(min_pin, max_pin)

# Iterate through PIN guesses within the specified range
for i in range(start_range, end_range + 1):
    guess = f"{i:0{num_digits}d}"  # Format the current guess as a string with leading zeros
    print(f"Trying PIN: {guess}")

    # Check if the current guess matches the generated PIN
    if guess == f"{pin:0{num_digits}d}":
        print(f"PIN found: {pin}")
        f = open("pin.txt", "w")
        print(pin, file=f)
        break  # Exit the loop if the correct PIN is found