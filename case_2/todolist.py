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
        input("Press enter to continue ")
        list_todos()
    elif operation == "add":
        print("-"*20)
        new_todo = input("New todo > ")
        print("-"*20)
        todos.append(new_todo)
        print("")
        print("Success: todo added")
        print("")
        input("Press enter to continue ")
        list_todos()
    elif operation == "delete":
        print("-"*20)
        i = 0
        for todo in todos:
            print("[" + str(i) + "] " + todo)
            i += 1
        print("-"*20)
        print("Select an index to delete a todo")
        while True:
            if i == 0:
                print("-"*20)
                print("No todos to delete")
                input("Press enter to continue ")
                break
            try:
                index = int(input("Delete todo > "))
                deleted_todo = todos.pop(index)
                print("Deleted todo :", deleted_todo)
                input("Press enter to continue ")
                break
            except ValueError:
                print("Error: invalid index")
                input("Press enter to try again ")
                print("-"*20)
            except IndexError:
                if index == 0:
                    todos = []
                    print("Deleted todo :", deleted_todo)
                    input("Press enter to continue ")
                    break
                else:
                    print("Error: index out of range")
                    input("Press enter to try again ")
                    print("-"*20)
        list_todos()

    elif operation == "load":
        f = open("Case/Case (GitHub)/case_grupp_55/case_2/todolist.json")
        todos = f.read()
        todos = json.loads(todos)
        f.close()
        list_todos()

    elif operation == "save":
        f = open("Case/Case (GitHub)/case_grupp_55/case_2/todolist.json", "w")
        print(todos)
        f.write(json.dumps(todos))
        f.close()
        list_todos()
list_todos()