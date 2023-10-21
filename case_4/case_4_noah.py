import requests
import json
import os
 
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
 
def print_basic_message():
    clear_terminal()
 
    print('****************************************')
    print('          FOOTBALL FRENZY')
    print('            STAT VIEWER')
    print('               1.0.0')
    print('----------------------------------------')
    print('| list | List available seasons')
    print('| view | View table for season')
    print('----------------------------------------')

def print_list(list):
    print('---------------------------------')
    for year in list:
        print(f'| {year}')

def api_request(api_url, stage):
    request = requests.get(api_url)
    status_check(request.status_code, stage)
    return json.loads(request.text)

def status_check(code, stage="Unknown"):
    if not (200 <= code < 300):
        print("Error: API request failed at " + stage + " api request, aborting")
        exit()

compare_goals = lambda a, b: 3 if a > b else (1 if a == b else 0)

while True:
    print_basic_message()

    input_selection = input('Selection > ')
    api_url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"
    main_dict = api_request(api_url, 'selection')

    if input_selection == 'list': 
        print_list(main_dict['seasons'])

    elif input_selection == 'view':
        print('---------------------------------')
        input_year = input('Year > ')

        year_url = api_url + '/' + input_year
        year_dict = api_request(year_url, 'year')
 
        print('****************************************')
        print('|')
        print('| Team                       Date      Points')
        print('| ---------------------      ---        ---')
 
        for team in year_dict['teams']:
            goals = 0
            for gameday in year_dict['gamedays']:

                team_url = year_url + '/' + gameday
                team_dict = api_request(team_url, 'gameday')

                for game in team_dict['games']:
                    
                    if game['score']['home']['team'] == team:
                        goals += compare_goals(int(game['score']['home']['goals']), int(game['score']['away']['goals']))
                    
                    elif game['score']['away']['team'] == team:
                        goals += compare_goals(int(game['score']['away']['goals']), int(game['score']['home']['goals']))
               
            print(f'| {team:<23} {team_dict["date"]:<13} {goals}')
 
    print('---------------------------------')
    input('Press enter to continue...')