def Calculate():
    print("""
****************************************
          Mathlete Calculator
----------------------------------------
 add | Add two numbers
 sub | Subtract two numbers
 mul | Multiply two numbers
 div | Divide two numbers
----------------------------------------""")

    selection = ""
    valid_selections = ["add", "sub", "mul", "div"]
    while selection not in valid_selections:
        selection = input("Selection > ")
        if selection in valid_selections:
            print("Selection accepted!")
            break
        else:
            print(f'''ERROR: Unknown command '{selection}' ''')

    if selection == "add":
        operator = "+"
    elif selection == "sub":
        operator = "-"
    elif selection == "mul":
        operator = "*"
    elif selection == "div":
        operator = "/"
    
    print(f'''----------------------------------------
Calculating 'c' for expression:

    a {operator} b = c

Please enter values for 'a' and 'b'.
''')

    while True:
        a = (input("a = "))
        b = (input("b = "))
        try:
            operation = a + " " + operator + " " + b
            c = eval(operation)
            break
        except NameError:
            print("""
Error: Invalid value
Retry
""")
        except ZeroDivisionError:
            print("""
Error: Attempted division by 0
Retry
""")

    print(f'''
RESULT: {operation} = {c}
''')

    input("Press enter to perform another operation...")
    Calculate()
Calculate()