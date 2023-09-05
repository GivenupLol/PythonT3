# DIGITECH Year 9 Term 3 Python Item 1

import os

# Define a function called phishing that takes a victim's name as an argument
def phishing(victim):
    print(f"""
============================================
     ~~~ Generating message now ~~~
============================================""")
    os.system("cls" if os.name == 'NT' else "clear")
    print(f"""
Dear {victim},

We have noticed some suspicious activity on your account.
The IT Department requires you to reset your password immediately to prevent a breach. 

      """)
      
    # Prompt the user for their old password and new passwords
    old = input("Old Password: ")
    new1 = input("New password: ")
    new2 = input("Confirm new password: ")
    
    # Check if the new passwords match, and loop until they do
    while new1 != new2:
        print("Passwords do not match. Please try again.")
        new1 = input("New password: ")
        new2 = input("Confirm new password: ")

    print()
    print("Thank you. Your password will be changed in the next 24-48 hours.")
    
    # Return the old password
    return old, new1

# Create an empty list to store harvested data
data = []

# Start an infinite loop to gather victim information
while True:
    os.system("cls" if os.name == 'NT' else "clear")
    victim = input("Phishing target (or 'EXIT' to exit): ")
    if victim == "EXIT":
        break
    if not victim:
        break
    # Call the phishing function to gather victim's data and store it in the list
    old_pass, new_pass = phishing(victim)
    data.append((victim, old_pass, new_pass))

print()

# Ask the user if they want to save the data to a text file
save = input("Would you like to save the data into a .txt file? (Y/N): ").lower()
if save == "y":
    # Ask for the name of the new data file or use the default name
    file = open("results1.txt", "w")  # Open the file in write mode

os.system("cls" if os.name == 'NT' else "clear")

if not data:
    exit()
else:
    print("Phishing successful, here is the data harvested from the attack:")

    # Iterate through the harvested data and print it
    for victim, old, new in data:
        if save == "y":
            print(f"user: '{victim}', old password: '{old}', new password: '{new}'", file=file)  # Write to the file
        print(f"user: '{victim}', old password: '{old}', new password: '{new}'")  # Print to the console
