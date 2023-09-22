import json
import os

todos = []

database_path = "case_grupp_55/case_2/todoify_database.json"

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_func():
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
    global todos

    selection = input("Selection > ")

    valid_selections = ['list', 'add', 'check', 'delete', 'save', 'load']
    if selection not in valid_selections:
        print(f'''----------------------------------------
              
ERROR: Unknown command "{selection}"
''')
    
    if selection == "list":
        print(40 * '-')
        if todos == []:
            print('No todos!')
        else:
            for todo in todos:
                print(f'[{todo[0]}] {todo[1]}')
        print(40 * '-')

    elif selection == "add":
        print(40 * '-')
        new_todo_element = input("Todo description > ")
        todos.append([" ", new_todo_element])
        print(f'''----------------------------------------
              
SUCCESS: Todo added "{new_todo_element}"
''')
    
    elif selection == 'check':
        print(40 * '-')

        i = 0
        for todo in todos:
            print(f'{str(i)} | [{todo[0]}] {todo[1]}')
            i += 1
        print(40 * '-')
        
        try:
            user_todo_id = int(input('Todo index > '))
            print(40 * '-')
            
            if todos[user_todo_id][0] == ' ':
                todos[user_todo_id][0] = 'X'
                print('''
SUCCESS: UNCHECKED -> CHECKED
''')
            else:
                todos[user_todo_id][0] = ' '
                print('''
SUCCESS: CHECKED -> UNCHECKED
''')
        except ValueError:
            print(f'''----------------------------------------
              
ERROR: Invalid index (must be a number)
''')
        except IndexError:
            print(f'''
ERROR: Invalid index (index out of range)
''')

    elif selection == "delete":
        print(40 * '-')

        i = 0
        for todo in todos:
            print(f'{str(i)} | [{todo[0]}] {todo[1]}')
            i += 1

        print(40 * '-')

        try:
            user_todo_id = int(input('Todo index > '))
            deleted_todo = todos.pop(user_todo_id)
            print(f'''----------------------------------------
              
SUCCESS: Todo deleted "{deleted_todo[1]}"
''')
        except ValueError:
            print(f'''----------------------------------------
              
ERROR: Invalid index (must be a number)
''')
        except IndexError:
            print(f'''----------------------------------------
            
ERROR: Invalid index (index out of range)
''')
        
    elif selection == "save":
        f = open(database_path, "w")
        f.write(json.dumps(todos))
        f.close()
        print(f'''----------------------------------------
              
SUCCESS: Todos saved to file
''')
        for todo in todos:
            print(f'''[{todo[0]}] {todo[1]}''')
        print('')

    elif selection == "load":
        f = open(database_path)
        todos = f.read()
        todos = json.loads(todos)
        f.close()
        print(f'''----------------------------------------
              
SUCCESS: Todos loaded from file
''')
        for todo in todos:
            print(f'''[{todo[0]}] {todo[1]}''')
        print('')
        
    input('Press enter to continue...')
    main_func()
main_func()