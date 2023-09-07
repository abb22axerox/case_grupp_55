def Calculate():
    print('''
****************************************
          Mathlete Calculator
----------------------------------------
 add | Add two numbers
 sub | Subtract two numbers
 mul | Multiply two numbers
 div | Divide two numbers
----------------------------------------''')

    selection = input("Selection > ")
    if selection == "add":
        operator = "+"
    elif selection == "sub":
        operator = "-"
    elif selection == "mul":
        operator = "*"
    elif selection == "div":
        operator = "/"
    else:
        print("Error: invalid selection (" + selection + ")")

    print(f'''----------------------------------------
Calculating 'c' for expression:

    a {operator} b = c

Please, enter values for 'a' and 'b'.
''')

    a = (input("a = "))
    b = (input("b = "))
    operation = a + " " + operator + " " + b
    c = eval(operation)

    print(f'''
RESULT: {operation} = {c}
''')

    input('Press enter to continue...')
    Calculate()
Calculate()