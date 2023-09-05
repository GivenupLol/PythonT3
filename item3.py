# DIGITECH Year 9 Term 3 Python Item 3

# Import the 'randint' function from the 'random' module
from random import randint

# Generate a random 4-digit PIN between 1000 and 9999 (inclusive)
pin = randint(1000, 10000)  # Note: The upper bound should be 10000 to include 9999

# Iterate through PIN guesses from 1000 to 9999
for i in range(1000, 10000):  # Note: The upper bound should be 10000 to include 9999
    guess = i  # Set the current guess to the loop iteration value
    print(f"Trying pin: {guess}")
    
    # Check if the current guess matches the generated PIN
    if guess == pin:
        print(f"Pin found: {pin}")
        break  # Exit the loop if the correct PIN is found
