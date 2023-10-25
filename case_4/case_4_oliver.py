import requests
import json
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def status_check(code, stage="Unknown"):
    if not (200 <= code < 300):
        print("Error: API request failed at stage: " + stage + ", aborting")
        exit()
        
def tally(home_name, home_score, away_name, away_score):
    for team in teams:
        if team["name"] == home_name:
            if home_score > away_score:
                team["wins"] += 1
            elif away_score > home_score:
                team["losses"] += 1
            else:
                team["draws"] += 1
        elif team["name"] == away_name:
            if away_score > home_score:
                team["wins"] += 1
            elif home_score > away_score:
                team["losses"] += 1
            else:
                team["draws"] += 1


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
            tally(game["score"]["home"]["team"], game["score"]["home"]["goals"], game["score"]["away"]["team"], game["score"]["away"]["goals"])

    print("-"*22)
    input("Fetch complete, press enter to continue ")
    clear()
    print("Season:", season["year"], "|", "Teams:", len(teams), "|", "Gamedays:", len(season["gamedays"]))
    print("*"*40)

    for team in teams:
        team["points"] = (team["wins"] * 3) + team["draws"]
    teams = sorted(teams, key=lambda x: x["points"], reverse=True)

    for team in teams:
        print(team["name"] + ":")
        print("[P]:", team["points"], "|", "[W]:", team["wins"], "|", "[D]:", team["draws"], "|", "[L]:", team["losses"])
        print("-"*37)
    input("Press enter to continue ")