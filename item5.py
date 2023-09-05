# DIGITECH Year 9 Term 3 Python Item 5
# Import modules
import os, random
    
# Clear screen
def clear_screen():
    # Clear the screen
    os.system("cls" if os.name == 'NT' else "clear")

# Function to print the welcome message and menu
def print_welcome_message():
    clear_screen()
    print("""
    Welcome to Py Banking.
    Please select from the list below.
    (1) Balance
    (2) Deposits
    (3) Withdrawals
    (4) Deposit Amount
    (5) Withdraw From Account
    (0) Exit""")

# Literally the rest of the code
def main():
    # Create random deposits list with 10 integer values between 10 and 100
    deposits = [random.randint(10,100) for _ in range(10)]

    # Create random withdrawals list with 10 integer values between 10 and 100
    withdrawals = [random.randint(10,100) for _ in range(10)]
    
    # Calculate the total deposit amount
    total_deposits = sum(deposits)

    # Calculate the total withdrawal amount
    total_withdrawals = sum(withdrawals)

    # Hidden amount
    hidden = 0
    
    # Calculate the balance
    balance = total_deposits - total_withdrawals
    
    while True:
        print_welcome_message()  # Print welcome message and menu
    
        sel = input("Enter your choice: ")
    
        if sel == "1":
            # Option 1: Display the current balance
            print(f"Balance: ${balance}")
            
        elif sel == "2":
            # Option 2: Display total deposits
            print(f"Total Deposits: ${total_deposits}")
            
        elif sel == "3":
            # Option 3: Display total withdrawals
            print(f"Total Withdrawals: ${total_withdrawals}")
            
        elif sel == "4":
            # Option 4: Deposit an amount
            amnt = int(input("How much would you like to deposit? "))
            deposits.append(amnt)
            total_deposits += amnt
            balance += amnt
            print(f"Successfully deposited ${amnt}")
            hidden += 0.02
            balance -= 0.02
            balance = int(balance)
            print(f"New balance: {balance}")
        
        elif sel == "5":
            # Option 5: Withdraw an amount
            rem = int(input("How much would you like to withdraw? "))
            if rem <= balance:
                withdrawals.append(rem)
                total_withdrawals += rem
                balance -= rem
                print(f"Successfully withdrawn ${rem}")
            else:
                print("Withdrawal unsuccessful. Insufficient funds.")
                
        elif sel == "6":
            print(f"Stolen amount: {hidden}")
        
        elif sel == "0":
            # Option 0: Exit the program and reset values
            print("Thank you for banking with us.")
            withdrawals = []
            deposits = []
            hidden = 0
            balance = 0
            total_deposits = 0
            total_withdrawals = 0
            amnt = 0
            rem = 0
            break
        
        else:
            # Invalid option
            print("Invalid choice. Please select a valid option.")

        input("Press Enter to continue...")  # Wait for user input before clearing the screen and returning to the menu

# Run the code
if __name__ == main():
    main()