# function necessary for re-using the code
def Calculate():
    # print
    print("""
****************************************
          Mathlete Calculator
----------------------------------------
 add | Add two numbers
 sub | Subtract two numbers
 mul | Multiply two numbers
 div | Divide two numbers
----------------------------------------""")

    # check if user input is valid
    selection = ""
    valid_selections = ["add", "sub", "mul", "div"]
    while selection not in valid_selections:
        selection = input("Selection > ")
        if selection in valid_selections:
            print("Selection accepted!")
            break
        else:
            print(f'''ERROR: Unknown command '{selection}' ''')

    # operators for calculating
    if selection == "add":
        operator = "+"
    elif selection == "sub":
        operator = "-"
    elif selection == "mul":
        operator = "*"
    elif selection == "div":
        operator = "/"
    
    # print
    print(f'''----------------------------------------
Calculating 'c' for expression:

    a {operator} b = c

Please enter values for 'a' and 'b'.
''')

    # user input numbers to calculate and check if it is valid
    while True:
        a = (input("a = "))
        b = (input("b = "))
        try:
            operation = a + " " + operator + " " + b
            c = eval(operation)
            break
        except (NameError, SyntaxError):
            print("""
Error: Invalid value
Retry
""")
        except ZeroDivisionError:
            print("""
Error: Attempted division by 0
Retry
""")

    # print
    print(f'''
RESULT: {operation} = {c}
''')

    input("Press enter to perform another operation...")
    Calculate() # calls the function to start again
Calculate() # necessary for initial start