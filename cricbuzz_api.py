import requests

API_KEY = "ab9f8c4c75msh3e6c95d5768fba5p1c4681jsn753d5ae37a43"

def get_live_matches():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
        "X-RapidAPI-Key":"ab9f8c4c75msh3e6c95d5768fba5p1c4681jsn753d5ae37a43",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"matches": []}
