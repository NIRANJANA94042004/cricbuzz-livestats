import requests

def get_live_matches():

    API_KEY = "ab9f8c4c75msh3e6c95d5768fba5p1c4681jsn753d5ae37a43"

    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
        "X-RapidAPI-Key":"ab9f8c4c75msh3e6c95d5768fba5p1c4681jsn753d5ae37a43",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    matches = []

    if "typeMatches" in data:
        for match_type in data["typeMatches"]:
            for series in match_type.get("seriesMatches", []):
                series_data = series.get("seriesAdWrapper", {})
                for match in series_data.get("matches", []):

                    info = match.get("matchInfo", {})
                    score = match.get("matchScore", {})

                    team1 = info.get("team1", {}).get("teamName", "")
                    team2 = info.get("team2", {}).get("teamName", "")

                    status = info.get("status", "")

                    matches.append({
                        "match_title": f"{team1} vs {team2}",
                        "status": status,
                        "score": []
                    })

    return {"matches": matches}
