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
    plainText = input('ENTER MESSAGE: ')
    # The key here means that the moving steps of the text so if the user enters letter A it will move to letter E
    key = jumps
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    # this is where the message appears after it has been encrypted
    cypherText = ' '

    plainText = plainText

    for letter in plainText:
        # we iterate throught the inputted values first
        if letter.lower() in ALPHABET:
            # then we check if the letters are contained in the alphabets using the find function
            num = ALPHABET.find(letter.lower())
            # when if finds the letter it will add the key to it which are the steps so if it finds letter A  the next letter becomes E
            num = num + key
            if num >= len(ALPHABET):
                # meaning if the keys are moved become longer than the alphabet
                num = num - len(ALPHABET)
            elif num < 0:
                num = num + len(ALPHABET)

            if letter == letter.lower():
                cypherText = cypherText + ALPHABET[num]
            else:
                cypherText = cypherText + ALPHABET[num].upper()
        else:
            cypherText = cypherText + letter
    print(cypherText)


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
        input("Press Enter to continue...")

    elif choice == "0":
        print("Exit")
        exit()

    else:
        print("The feature has not been implemented yet, please check back for updates.")
