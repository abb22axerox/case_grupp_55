import requests
import json
import os

url = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"

re = requests.get(url)
status = re.status_code
if status == 200:
    artists = json.loads(re.text)["artists"]

    def clear():
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

    def print_menu():
        clear() 
        print(".: Artist Database :.".center(32))
        print("*"*32)

    def list_artists():
        print_menu()
        for artist in artists:
            print("-", artist["name"])
            print("-"*32)

    def fetch_artist():
        re = requests.get(url)
        status = re.status_code
        if 200 <= status < 300:

            artists = json.loads(re.text)["artists"]
            for artist in artists:
                if artist["name"].lower() == selection:
                    re = requests.get(url + artist["id"])
                    status = re.status_code
                    if 200 <= status < 300:
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
                    
                    else:
                        print("Error: API failed to complete request")
                        exit()
        else:
            print("Error: API failed to complete request")
            exit()

    while True:
        print_menu()
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

            print_menu()
            for artist in artists:
                if artist["name"].lower() == selection:
                    print("Fetching ", artist["name"] + "...")
                    print("-"*32)
                    fetch_artist()
                    break
            else:
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

else:
    print("Error: API failed to complete request")