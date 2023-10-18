import requests
import json
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_basic_message():
    clear_terminal()

    print('''****************************************
          FOOTBALL FRENZY
            STAT VIEWER
               1.0.0
----------------------------------------
| list | List available seasons
| view | View table for season
----------------------------------------''')
    
while True:
    print_basic_message()
    selection = input('Selection > ')

    api_url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"

    r = requests.get(api_url)
    main_dict = json.loads(r.text)


    if selection == 'list':
        print(40 * '-')
        for year in main_dict['seasons']:
            print(f'| {year}')


    elif selection == 'view':
        print(40 * '-')
        usr_year = input('Year > ')
        year_url = api_url + '/' + usr_year

        r = requests.get(year_url)
        year_dict = json.loads(r.text)

        print('''****************************************
|
| Team                     Date   Points
| ---------------------    ---    ---''')

        for team in year_dict['teams']:
            goals = 0
            for gameday in year_dict['gamedays']:
                team_url = year_url + '/' + gameday
                r = requests.get(team_url)
                team_dict = json.loads(r.text)
                for game in team_dict['games']:
                    if game['score']['home']['team'] == team or game['score']['away']['team'] == team:
                        
                        # if home team won
                        if game['score']['home']['team'] == team:
                            if int(game['score']['home']['goals']) > int(game['score']['away']['goals']):
                                goals += 3
                        
                        # if away team won
                        elif game['score']['away']['team'] == team:
                            if int(game['score']['away']['goals']) > int(game['score']['home']['goals']):
                                goals += 3

                        # if draw
                        if int(game['score']['home']['goals']) == int(game['score']['away']['goals']):
                            goals += 1
                
            print(f'| {team}   {team_dict["date"]}   {goals}')

    print(40 * '-')
    input('Press enter to continue...')