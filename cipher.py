jumps = 0
choice = " "



def getName():
    print("Hello, what is your name? ")
    name = str(input(" "))
    print("Hello, name")
    return name

def getInput():
    x = str(input( ))
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
while (choice.lower() !="exit"):
    print('''
    1. Instantiate encryption parameters
    2. Encrypt text
    3. Decrypt text
    4. Reset encryption parameters
    5. History
    ''')

    print("Enter the number that corresponds with the task you want to perform ")
    choice = input( )

    if choice == "1":
        jumps = instantiate()
        print(f'jumps instantiated to {jumps}')

    elif choice == "2":
        encrypt()




   