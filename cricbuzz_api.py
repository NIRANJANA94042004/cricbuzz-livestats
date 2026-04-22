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

                    score_list = []

                    if "team1Score" in score:
                        t1 = score["team1Score"].get("inngs1", {})
                        score_list.append({
                            "short": team1,
                            "score": f'{t1.get("runs", "")}/{t1.get("wickets", "")}'
                        })

                    if "team2Score" in score:
                        t2 = score["team2Score"].get("inngs1", {})
                        score_list.append({
                            "short": team2,
                            "score": f'{t2.get("runs", "")}/{t2.get("wickets", "")}'
                        })

                    matches.append({
                        "match_title": f"{team1} vs {team2}",
                        "status": status,
                        "score": score_list
                    })

    return {"matches": matches}
