from datetime import datetime


jumps = 0
choice = " "
logs = []


def instantiate():
    print("What is your preferred number of character jumps? ")
    try:
        jumps = int(input(' '))
        return jumps
    except ValueError:
        print("Error! please enter a number between 1-26")
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
    logs.append(
        f'encryption  -  {plainText}  -  {cypherText}  -  {datetime.now()}')

    # return cypherText


# logs.append(encrypt())


def decrypt():
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
            # when if finds the letter it will subtract the key to it which are the steps so if it finds letter A  the next letter becomes X
            num = num - key
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
    logs.append(
        f'decryption  -  {plainText}  -  {cypherText}  -  {datetime.now()}')

    # return cypherText
    # logs.append(decrypt())


def history():
    print(logs)
