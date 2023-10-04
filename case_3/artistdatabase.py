import requests
import json
import os

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

re = requests.get("https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/")
artists = json.loads(re.text)["artists"]

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def find_artist(a):
    clear()
    print(".: Artist Database :.".center(24))
    print("*"*24)
    global artists
    for artist in artists:
        if artist["name"].lower() == a:
            print("Fetching information about", artist["name"] + "...")
            print("-"*24)

            re = requests.get(url)
            artists = json.loads(re.text)["artists"]

            for artist in artists:
                if artist["name"].lower() == a:
                    re = requests.get(url + artist["id"])
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
                    
                    print("-"*24)

def list_artists():
    clear() 
    print(".: Artist Database :.".center(24))
    print("*"*24)
    for artist in artists:
        print("-", artist["name"])
        print("-"*24)

while True:
    clear()
    print(".: Artist Database :.".center(24))
    print("*"*24)
    print("| L |  List artists")
    print("| V |  View artist profile")
    print("| E |  Exit application")
    print("-"*24)

    op = input("> ")
    print("-"*24)
    if op == "L":
        list_artists()

    elif op == "V":
        selection = input("View the profile of > ").lower()
        print("-"*24)
        find_artist(selection)

    elif op == "E":
        print("Exiting application...")
        exit()

    else:
        print("Invalid operation")
        print("-"*24)

    input("Press enter to continue ")