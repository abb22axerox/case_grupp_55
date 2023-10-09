import requests
import json
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def status_check(code):
    if not (200 <= code < 300):
        print("Error: API request failed, aborting")
        exit()

def print_header():
    clear() 
    print(".: Artist Database :.".center(32))
    print("*"*32)

def list_artists():
    print_header()
    for artist in artists:
        print("-", artist["name"])
        print("-"*32)

def fetch_artist():
    re = requests.get(url)
    status_check(re.status_code)
    artists = json.loads(re.text)["artists"]

    for artist in artists:
        if artist["name"].lower() == selection:
            re = requests.get(url + artist["id"])
            status_check(re.status_code)
            info = json.loads(re.text)["artist"]

            print("Name:", info["name"])
            print()

            if len(info["members"]) > 1:
                print("Members:")
                for member in info["members"]:
                    print("  -", member)
                print()

            if len(info["genres"]) > 1:
                print("Genres:")
                for genre in info["genres"]:
                    print("  -", genre)
            else:
                print("Genre:", info["genres"][0])
            print()
                                
            if len(info["years_active"]) > 1:
                print("Active:")
                for period in info["years_active"]:
                    print("  -", period)
            else:
                print("Active:", info["years_active"][0])
            print()
                                
            print("-"*32)
            break


url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

re = requests.get(url)
status_check(re.status_code)
artists = json.loads(re.text)["artists"]

while True:
    print_header()
    print("| L |  List artists")
    print("| V |  View artist profile")
    print("| E |  Exit application")
    print("-"*32)

    op = input("> ").upper()
    print("-"*32)
    if op == "L":
        list_artists()

    elif op == "V":
        selection = input("View the profile of > ").lower()
        for artist in artists:
            if artist["name"].lower() == selection:
                print_header()
                print("Fetching ", artist["name"] + "...")
                print("-"*32)
                fetch_artist()
                break
        else:
            print("-"*32)
            print("No artist or band named", selection, "found")
            print("-"*32)

    elif op == "E":
        print("Exiting application...")
        print("-"*32)
        exit()

    else:
        print("Invalid operation")
        print("-"*32)

    input("Press enter to continue ")