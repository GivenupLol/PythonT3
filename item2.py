# DIGITECH Year 9 Term 3 Python Item 2

# Define a function to check if a password is common and return its position
def common_password_position(password):
    # Open and read the list of common passwords from a file
    with open("passwords.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                common_password = parts[0].strip()
                if password == common_password:
                    return int(parts[1].strip())  # Return the position of the common password
        return None  # Return None if the password is not common
    
# Get user input for the password
passwd = input("Password: ")

position = common_password_position(passwd)

# Define a string containing punctuation characters
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

# Calculate various password attributes
length = len(passwd)
numbers = sum(1 for char in passwd if char.isdigit())       # Count of digits
letters = sum(1 for char in passwd if char.isalpha())       # Count of letters
capitals = sum(1 for char in passwd if char.isupper())      # Count of uppercase letters
lowercase = sum(1 for char in passwd if char.islower())     # Count of lowercase letters
spaces = sum(1 for char in passwd if char.isspace())            # Count of spaces
specialchars = sum(1 for char in passwd if char in punctuation) # Count of special characters

# Print various password attributes
if position is not None:
    if 10 <= position % 100 <= 20:
        suffix = "th"
    else:
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        suffix = suffixes.get(position % 10, "th")
    print(f"Your password is the {position}{suffix} most common password.")
else:
    print("Your password is not common. ")
    
print(f"Length: {length}")
print(f"Numbers: {numbers}")
print(f"Letters: {letters}")
print(f"Capitals: {capitals}")
print(f"Lowercase: {lowercase}")
print(f"Spaces: {spaces}")
print(f"Special Characters: {specialchars}")

# Check if the password meets the criteria for strength
if length >= 6 and capitals >= 1 and numbers >= 1 and specialchars >= 1:
    strong = True
else:
    strong = False

# Print the strength assessment
if strong:
    print("Strength: OK")
else:
    print("Strength: Weak")

