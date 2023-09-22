import json
import os

todos = []

def list_todos():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    
    global todos

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
        for todo in todos:
            if todo[0] == "checked":
                check = "[X]"
            else:
                check = "[]"
            print(check, todo[1])
        print("-"*20)
        input("Press enter to continue ")
        list_todos()
    elif operation == "add":
        print("-"*20)
        new_todo_element = input("New todo > ")
        print("-"*20)
        new_todo = ["unchecked", new_todo_element]
        todos.append(new_todo)
        print("-"*20)
        print("Todo added: " + new_todo_element)
        print("-"*20)
        input("Press enter to return to menu ")

    elif operation == "check":
        print("*"*20)
        print("Todos".center(20))
        print("-"*20)
        i = 0
        for todo in todos:
            if todo[0] == "checked":
                check = "[X]"
            else:
                check = "[]"
            print("[" + str(i) + "]", check,  todo[1])
            i += 1

        if i == 0:
            print("No todos to check/uncheck")
            print("-"*20)
            input("Press enter to return to menu ")
        
        else: 
            print("-"*20)
            print("Select an index to check/uncheck a todo")
            print("-"*20)
            
            try:
                index = int(input("Check / Uncheck todo > "))
                if todos[index][0] == "unchecked":
                    todos[index][0] = "checked"
                    print("-"*20)
                    print("Checked todo :", todos[index][1])
                else: 
                    todos[index][0] = "unchecked"
                    print("-"*20)
                    print("Unchecked todo :", todos[index][1])
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

    elif operation == "delete":
        print("-"*20)
        i = 0
        for todo in todos:
            print("[" + str(i) + "]", todo[1])
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
                print("-"*20)
                print("Deleted todo :", deleted_todo[1])
                print("-"*20)
                input("Press enter to return to menu ")

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
        print("-"*20)
        print("Todolist loaded")
        print("-"*20)
        input("Press enter to return to menu ")

    elif operation == "save":
        f = open("Case/Case (GitHub)/case_grupp_55/case_2/todolist.json", "w")
        f.write(json.dumps(todos))
        f.close()
        print("-"*20)
        print("Todolist saved")
        print("-"*20)
        input("Press enter to return to menu ")

    else:
        print("-"*20)
        print("Invalid operation")
        print("-"*20)
        input("Press enter to return to menu ")

    list_todos()
list_todos()