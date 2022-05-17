jumps = 0
choice = " "


def getName():
    print("Hello, what is your name? ")
    name = str(input(" "))
    print("Hello, name")
    return name


def getInput():
    x = str(input())
    return x


def instantiate():
    print("What is your preferred number of character jumps? ")
    jumps = int(input(' '))
    return jumps
    # setup character jumps


def encrypt():
    pass


def decrypt():
    pass


def reset():
    pass


def history():
    pass


# to display a menu
print("press '0' to exit")

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
        jumps = instantiate()
        print(f'jumps instantiated to {jumps}')
        input("Press Enter to continue...")

    elif choice == "2":
        encrypt()

    elif choice == "0":
        print("Exit")
        exit()

    else:
        print("The feature has not been implemented yet, please check back for updates.")
