import os

f = open('todoify_database.csv', 'r')
csv = f.read()
f.close()
rows = csv.split('\n')  # str -> list
rows.remove(rows[0]) # removes first line

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_message(message_type):
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

    if message_type == 'add':

        print(40 * '-')

        user_add = input('Todo description > ')

        print('''SUCCESS: Todo added''')

        input('Press enter to continue...')

        print_message('start')

    elif message_type == 'delete':
        print()

def print_todos(message_type, columns):

    if message_type == 'list':
        print(f'{columns[1]}')

    elif message_type == 'check':
        print(f'{columns[0]} | [{columns[2]}] {columns[1]}')

def main_func():
    print_message('start')

    selection = input('Selection > ')

    for row in rows:
        columns = row.split(',')

        if selection == 'list':
            print_todos('list', columns)

        elif selection == 'check':
            print_todos('check', columns)


    if selection == 'check':
        user_todo_id = input('Todo index > ')

        for column in columns:
            if user_todo_id == column[0]:
                if column[2] == ' ':
                    # column[2] = 'X'
                    print('SUCCESS: UNCHECKED -> CHECKED')
                else:
                    # column[2] = ' '
                    print('SUCCESS: CHECKED -> UNCHECKED')

    if selection == 'add':
        print()

    elif selection == 'delete':
        print()

    elif selection == 'save':
        print()

    elif selection == 'load':
        print()

    input('Press enter to continue...')
    main_func()
main_func()

