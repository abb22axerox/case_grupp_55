import requests
import json
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def status_check(code, stage="Unknown"):
    if not (200 <= code < 300):
        print("Error: API request failed at stage: " + stage + ", aborting")
        exit()
        
def tally(t, w=0, d=0, l=0):
    for team in teams:
        if team["name"] == t:
            team["wins"] += w
            team["draws"] += d
            team["losses"] += l
            team["points"] += ((w * 3) + d)
            break

url = "http://football-frenzy.s3-website.eu-north-1.amazonaws.com/api"

i_fetch = requests.get(url)
status_check(i_fetch.status_code, "Initial Fetch")
response_text = json.loads(i_fetch.text)

while True:
    clear()
    print("Seasons:", response_text["seasons"][0] + "-" + response_text["seasons"][-1])
    print("-"*22)
    selection = input("Season > ")
    print("-"*22)

    for i, season in enumerate(response_text["seasons"]):
        if season == selection:
            season_url = url + "/" + response_text["seasons"][i]
            break
    else:
        print("Error: invalid season")
        print("-"*22)
        input("Press enter to continue ")
        continue

    s_fetch = requests.get(season_url)
    status_check(s_fetch.status_code, "Season Fetch")
    season = json.loads(s_fetch.text)

    teams = []
    for team in season["teams"]:
        teams.append({
            "name": team,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "points": 0
        })

    for i, day in enumerate(season["gamedays"]):
        gameday_url = season_url + "/" + season["gamedays"][i]
        gd_fetch = requests.get(gameday_url)
        status_check(gd_fetch.status_code, "Gameday Fetch")
        gameday = json.loads(gd_fetch.text)

        print("Fetching day", gameday["date"][5:] + "...")
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

    print("-"*22)
    input("Fetch complete, press enter to continue ")
    clear()
    print("Season:", season["year"], "|", "Teams:", len(teams), "|", "Gamedays:", len(season["gamedays"]))
    print("*"*40)

    teams = sorted(teams, key=lambda x: x["points"], reverse=True)

    for team in teams:
        print(team["name"] + ":")
        print("[P]:", team["points"], "|", "[W]:", team["wins"], "|", "[D]:", team["draws"], "|", "[L]:", team["losses"])
        print("-"*37)
    input("Press enter to continue ")