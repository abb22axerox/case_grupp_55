import os
import requests
import json

api_url = 'https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/'

main_dict = requests.get(api_url)
main_dict = json.loads(main_dict.text)

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_instructions():
    print('''| L | List artists
| V | View artist profile
| E | Exit application
----------------------------------------''')

def print_basic_message():
    clear_terminal()
    print('''----------------------------------------
            Artists Database
----------------------------------------''')

print_basic_message()
print_instructions()

while True:
    selection = input('| Selection > ').lower()

    if selection == 'l':
        print_basic_message()
        for artist in main_dict['artists']:
            print(f"| {artist['name']}")
        print(40 * '*')
        print_instructions()
    
    elif selection == 'v':
        print_basic_message()
        name = input('| Artist name > ').lower().title()
        match = False

        for artist in main_dict['artists']:
            if name == artist['name']:
                artist_url = api_url + artist['id']
                match = True
        
        if match:
            artist_dict = requests.get(artist_url)
            artist_dict = json.loads(artist_dict.text)

            genre_str = ''
            for genre in artist_dict['artist']['genres']:
                genre_str += genre + ', '

            print(f"""****************************************
               {artist_dict['artist']['name']}
****************************************
| Members:      {artist_dict['artist']['members'][0]}
| Genres:       {genre_str[:-2]}
| Years Active: {artist_dict['artist']['years_active'][0]}
----------------------------------------""")
        else:
            print(f'''----------------------------------------
|
| ERROR: Artist not found '{name}'
|
----------------------------------------''')
        print_instructions()

    elif selection == 'e':
        break
    
    else:
        input(f'''----------------------------------------
|
| ERROR: Unknown command '{selection}'
|
----------------------------------------
Press enter to continue...''')
        print_basic_message()
        print_instructions()