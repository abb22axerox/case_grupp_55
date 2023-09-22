import json
import os

todos = []

def list_todos():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

    print("*"*20)
    print("Todoify".center(20))
    print("-"*20)
    print("list   | List todos")
    print("add    | Add todo")
    print("check  | Check todo")
    print("delete | Delete todo")
    print("-"*20)
    print("save   | Save todos to file")
    print("load   | Load todos from file")
    print("-"*20)

    operation = input("Selection > ")
    if operation == "list":
        print("*"*20)
        print("Todos".center(20))
        print("-"*20)
        global todos
        for todo in todos:
            print("[] " + todo)
        print("-"*20)
        input("Press enter to return to menu ")

    elif operation == "add":
        print("-"*20)
        new_todo = input("New todo > ")
        todos.append(new_todo)
        print("-"*20)
        print("Todo added: " + new_todo)
        print("-"*20)
        input("Press enter to return to menu ")

    elif operation == "delete":
        print("-"*20)
        i = 0
        for todo in todos:
            print("[" + str(i) + "] " + todo)
            i += 1

        if i == 0:
            print("No todos to delete")
            print("-"*20)
            input("Press enter to return to menu ")

        else: 
            print("-"*20)
            print("Select an index to delete a todo")
            
            try:
                index = int(input("Delete todo > "))
                deleted_todo = todos.pop(index)
                print("-"*20)
                print("Deleted todo :", deleted_todo)
                print("-"*20)
                input("Press enter to return to menu ")

            except ValueError:
                print("-"*20)
                print("Error: invalid index")
                print("-"*20)
                input("Press enter to return to menu ")

            except IndexError:
                print("-"*20)
                print("Error: index out of range")
                print("-"*20)
                input("Press enter to return to menu ")

    elif operation == "load":
        f = open("Case/Case (GitHub)/case_grupp_55/case_2/todolist.json")
        todos = f.read()
        todos = json.loads(todos)
        f.close()
        print("-"*20)
        input("Todolist loaded")
        print("-"*20)
        input("Press enter to return to menu ")

    elif operation == "save":
        f = open("Case/Case (GitHub)/case_grupp_55/case_2/todolist.json", "w")
        print(todos)
        f.write(json.dumps(todos))
        f.close()
        print("-"*20)
        input("Todolist saved")
        print("-"*20)
        input("Press enter to return to menu ")

    else:
        print("-"*20)
        print("Invalid operation")
        print("-"*20)
        input("Press enter to return to menu ")

    list_todos()
list_todos()