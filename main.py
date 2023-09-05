import os


    
def run(scriptname):
    with open(scriptname, 'r') as file:
        scode = file.read()
        exec(scode, globals())
    input("\nPress Enter to continue...")
    
def main():
    while True:
        os.system("cls" if os.name == 'NT' else "clear")
        print("""
Welcome to Adam's Term 3 DIGITECH Assignment

Scripts
(1) desc
(2) desc
(3) desc
(4) desc
(5) desc

(0) Exit""")
        choice = int(input("\nPlease select which script to run: "))

        if choice == 1:
            script = "item1.py"
            os.system("cls" if os.name == 'NT' else "clear")
            run(script)
        elif choice == 2:
            os.system("cls" if os.name == 'NT' else "clear")
            script = "item2.py"
            run(script)
        elif choice == 3:
            os.system("cls" if os.name == 'NT' else "clear")
            script = "item3.py"
            run(script)
        elif choice == 4:
            os.system("cls" if os.name == 'NT' else "clear")
            script = "item4.py"
            run(script)
        elif choice == 5:
            os.system("cls" if os.name == 'NT' else "clear")
            script = "item5.py"
            run(script)
        
        elif choice == 0:
            break
        
        else:
            print("Invalid choice")
            choice = int(input("\nPlease select which script to run: "))
            
if __name__ == "__main__":
    main()