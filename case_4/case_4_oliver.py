import requests
import json
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def status_check(code, stage="Unknown"):
    if not (200 <= code < 300):
        print("Error: API request failed at stage: " + stage + ", aborting")
        exit()
        
def tally(t, w=0, d=0, l=0):
    for team in a_teams:
        if team["name"] == t:
            team["wins"] += w
            team["draws"] += d
            team["losses"] += l
            team["points"] += ((w * 3) + d)

url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"

i_fetch = requests.get(url)
status_check(i_fetch.status_code, "Initial Fetch")
re = json.loads(i_fetch.text)

while True:
    clear()
    print("Available seasons:", re["seasons"][0], "---", re["seasons"][-1])
    print("-"*40)
    selection = input("Season > ")
    print("-"*40)

    for i, season in enumerate(re["seasons"]):
        if season == selection:
            season_url = url + "/" + re["seasons"][i]
            break
    else:
        print("Error: invalid season")
        print("-"*40)
        input("Press enter to continue ")
        continue

    s_fetch = requests.get(season_url)
    status_check(s_fetch.status_code, "Season Fetch")
    season = json.loads(s_fetch.text)

    a_teams = []
    for team in season["teams"]:
        a_teams.append({
            "name": team,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "points": 0
        })

    for i, day in enumerate(season["gamedays"]):
        gameday_url = season_url + "/" + season["gamedays"][i]
        g_fetch = requests.get(gameday_url)
        status_check(g_fetch.status_code, "Gameday Fetch")
        gameday = json.loads(g_fetch.text)

        print("Fetching day", gameday["date"] + "...")
        for game in gameday["games"]:
            h_name = game["score"]["home"]["team"]
            h_score = game["score"]["home"]["goals"]

            a_name = game["score"]["away"]["team"]
            a_score = game["score"]["away"]["goals"]

            if h_score > a_score:
                tally(h_name, w=1)
                tally(a_name, l=1)
            elif h_score < a_score:
                tally(a_name, w=1)
                tally(h_name, l=1)
            else:
                tally(a_name, d=1)
                tally(h_name, d=1)

    print("-"*40)
    input("Fetch complete, press enter to continue ")
    clear()
    print("Season:", season["year"], "-", "Teams:", len(a_teams), "-", "Gamedays:", len(season["gamedays"]))
    print("*"*40)

    a_teams = sorted(a_teams, key=lambda x: x["points"], reverse=True)

    for team in a_teams:
        print(team["name"] + ":")
        print("[P]:", team["points"], "|", "[W]:", team["wins"], "|", "[D]:", team["draws"], "|", "[L]:", team["losses"])
        print("-"*40)
    input("Press enter to continue ")