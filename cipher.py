def getName():
    print("Hello, what is your name? ")
    name = str(input(" "))
    print("Hello, name")
    return name

    # to display a menu
 
print('''
1. Instantiate encryption parameters
2. Encrypt
3. Decrypt text
4. Reset encryption parameters
5. History
''')

print("Enter the number that corresponds with the task you want to perform ")
choice = int(input( ))
