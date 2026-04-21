import requests

def get_live_matches():
    url = "https://cric-buzz-cricket-live.p.rapidapi.com/matches/live"

    headers = {
        "X-RapidAPI-Key": "ab9f8c4c75msh3e6c95d5768fba5p1c4681jsn753d5ae37a43",
        "X-RapidAPI-Host": "cric-buzz-cricket-live.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response.json()