def getName():
    print("Hello, what is your name? ")
    name = str(input(" "))
    print("Hello, name")
    return name
    


def getInput():
    x = str(input( ))
    return x


def instantiate():
    x = getInput()
    print("What is your preferred number of character jumps? ")
    jumps = int(input( ))
    return jumps

def encrypt():
    pass

def decrypt():
    pass

def reset():
    pass

def history():
    pass

  

# to display a menu
 
print('''
1. Instantiate encryption parameters
2. Encrypt
3. Decrypt text
4. Reset encryption parameters
5. History
''')

print("Enter your the number that corresponds with the task you want to perform ")
choice = int(input( ))

task = [instantiate, encrypt, decrypt, reset, history]

result = task [choice-1]()

print(result)