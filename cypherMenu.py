
import cipher

choice = " "

# to display a menu
print("press '0'to exit")

while (choice.lower() != "0"):
    print('''
    1. Instantiate encryption parameters
    2. Encrypt text
    3. Decrypt text
    4. Reset encryption parameters
    5. History
    ''')

    print("Enter the number that corresponds with the task you want to perform: ")
    choice = input()

    if choice == "1":
        cipher.jumps = cipher.instantiate()
        print(f'jumps instantiated to {cipher.jumps}')
        input("Press Enter to continue...")

    elif choice == "2":
        cipher.encrypt()
        input("Press Enter to continue...")

    elif choice == "3":
        cipher.decrypt()
        input("Press Enter to continue...")

    elif choice == "0":
        print("Exit")
        exit()

    elif choice == "4":
        cipher.jumps = 0
        print("Restarting...")
        print("Enter new ecryption parameters")
        input("Press Enter to continue...")

    elif choice == "5":
        cipher.history()

    else:
        print("The feature has not been implemented yet, please check back for updates.")
