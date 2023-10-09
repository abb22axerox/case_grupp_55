import requests
import json
import os

api_url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def status_check(code):
    if not (200 <= code < 300):
        print('Error: API request failed, aborting')
        exit()

def print_header():
    clear_terminal() 
    print('''--------------------------------
        Artists Database
********************************''')

def list_artists():
    print_header()
    for artist in artists:
        print(f'- {artist["name"]}')
    print(32 * '-')

def fetch_artist():
    api_data = requests.get(api_url)
    status_check(api_data.status_code)
    artists = json.loads(api_data.text)["artists"]

    for artist in artists:
        if artist["name"].lower() == selection:
            api_data = requests.get(api_url + artist["id"])
            status_check(api_data.status_code)
            artist_data = json.loads(api_data.text)["artist"]

            # prints members
            if len(artist_data["members"]) > 1:
                print('Members:')
                for member in artist_data["members"]:
                    print(f'- {member}')
                print()
            elif artist_data["members"][0] != artist_data["name"]:
                print(f'''Real name:
  {artist_data["members"][0]}
''')

            # prints genres
            if len(artist_data["genres"]) > 1:
                print('Genres:')
                for genre in artist_data["genres"]:
                    print(f'- {genre}')
            else:
                print(f'Genre: {artist_data["genres"][0]}')
            print()
            
            # print years active
            if len(artist_data["years_active"]) > 1:
                print('Active:')
                for period in artist_data["years_active"]:
                    print(f'- {period}')
            else:
                print(f'Active: {artist_data["years_active"][0]}')
            print()

            print(32 * '-')
            break

api_data = requests.get(api_url)
status_check(api_data.status_code)
artists = json.loads(api_data.text)["artists"]

while True:
    print_header()
    print('''| L | List artists
| V | View artist profile
| E | Exit application
--------------------------------''')

    selection = input('| Selection > ').upper()

    print(32 * '-')

    if selection == "L":
        list_artists()

    elif selection == "V":
        selection = input('View the profile of > ').lower()
        for artist in artists:
            if artist["name"].lower() == selection:
                print_header()
                print(f'Fetching {artist["name"]}...')
                print(32 * '-')
                fetch_artist()
                break
        else:
            print("-"*32)
            print(f'No artist or band named "{selection}" found')
            print(32 * '-')

    elif selection == "E":
        print('Exiting application...')
        print(32 * '-')
        exit()

    else:
        print(f'Invalid operation "{selection}"')
        print(32 * '-')

    input('Press enter to continue... ')