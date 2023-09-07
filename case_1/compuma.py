def Calculate():
    print("********************************")
    print("       MATHLETE CALCULATOR      ")
    print("--------------------------------")
    print(" add | Add two numbers")
    print(" sub | Subract two numbers")
    print(" mul | Multiply two numbers")
    print(" div | Divide two numbers")
    print("--------------------------------")

    selection = ""
    valid_selections = ["add", "sub", "mul", "div"]
    while selection not in valid_selections:
        selection = input("Selection > ")
        if selection in valid_selections:
            print("Selection accepted!")
            print("")
            break
        else:
            print("Error: Invalid selection (" + selection + ")")

    if selection == "add":
        operator = "+"
    elif selection == "sub":
        operator = "-"
    elif selection == "mul":
        operator = "*"
    elif selection == "div":
        operator = "/"

    print("--------------------------------")
    print(" Calculating 'c' for expression:")
    print("")
    print("a " + operator + " b = c")
    print("")
    print("Enter values for 'a' and 'b'")
    print("")

    while True:
        a = (input("a = "))
        b = (input("b = "))
        try:
            operation = a + " " + operator + " " + b
            c = eval(operation)
            break
        except NameError:
            print("Error: Invalid value")
            print("Retry")
            print("")
        except ZeroDivisionError:
            print("Error: Attempted division by 0")
            print("Retry")
            print("")

    print("--------------------------------")
    print("")
    print("Result:", operation, "=", c)
    print("")

    input("Press enter to perform another calculation ")
    Calculate()
Calculate()