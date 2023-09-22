import json
import os

todos = []

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_todos():
    clear_terminal()

    print('''****************************************
                Todoify
----------------------------------------
list   | List todos
add    | Add todo
check  | Check todo
delete | Delete todo
----------------------------------------
save   | Save todos in a file
load   | Load todos from file
----------------------------------------''')

    selection = input("Selection > ")
    
    if selection == "list":
        print("*"*20)
        print("Todos".center(20))
        print("-"*20)
        global todos
        for todo in todos:
            print("[] " + todo)
        print("-"*20)

    elif selection == "add":
        print("-"*20)
        new_todo = input("New todo > ")
        todos.append(new_todo)
        print("-"*20)
        print("Todo added: " + new_todo)
        print("-"*20)

    elif selection == "delete":
        print("-"*20)
        i = 0
        for todo in todos:
            print("[" + str(i) + "] " + todo)
            i += 1

        if i == 0:
            print("No todos to delete")
            print("-"*20)

        else: 
            print("-"*20)
            print("Select an index to delete a todo")
            
            try:
                index = int(input("Delete todo > "))
                deleted_todo = todos.pop(index)
                print("-"*20)
                print("Deleted todo :", deleted_todo)
                print("-"*20)

            except ValueError:
                print("-"*20)
                print("Error: invalid index")
                print("-"*20)

            except IndexError:
                print("-"*20)
                print("Error: index out of range")
                print("-"*20)

    elif selection == "load":
        f = open("Case/Case (GitHub)/case_grupp_55/case_2/todolist.json")
        todos = f.read()
        todos = json.loads(todos)
        f.close()
        print("-"*20)
        input("Todolist loaded")
        print("-"*20)

    elif selection == "save":
        f = open("Case/Case (GitHub)/case_grupp_55/case_2/todolist.json", "w")
        print(todos)
        f.write(json.dumps(todos))
        f.close()
        print("-"*20)
        input("Todolist saved")
        print("-"*20)

    else:
        print("-"*20)
        print("Invalid selection")
        print("-"*20)
        
    input('Press enter to continue...')
    list_todos()
list_todos()