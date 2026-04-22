import requests

API_KEY = "ab9f8c4c75msh3e6c95d5768fba5p1c4681jsn753d5ae37a43"

def get_live_matches():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/live"

    headers = {
        "X-RapidAPI-Key":"ab9f8c4c75msh3e6c95d5768fba5p1c4681jsn753d5ae37a43",
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        matches = []

        if "typeMatches" in data:
            for match_type in data["typeMatches"]:
                for series in match_type.get("seriesMatches", []):
                    series_data = series.get("seriesAdWrapper", {})
                    for match in series_data.get("matches", []):
                        match_info = match.get("matchInfo", {})
                        match_status = match.get("matchScore", {})

                        team1 = match_info.get("team1", {}).get("teamName", "")
                        team2 = match_info.get("team2", {}).get("teamName", "")
                        status = match_info.get("status", "")

                        score = []

                        if "team1Score" in match_status:
                            t1 = match_status["team1Score"].get("inngs1", {})
                            score.append({
                                "short": team1,
                                "score": f'{t1.get("runs", "")}/{t1.get("wickets", "")}'
                            })

                        if "team2Score" in match_status:
                            t2 = match_status["team2Score"].get("inngs1", {})
                            score.append({
                                "short": team2,
                                "score": f'{t2.get("runs", "")}/{t2.get("wickets", "")}'
                            })

                        matches.append({
                            "match_title": f"{team1} vs {team2}",
                            "status": status,
                            "score": score
                        })

        return {"matches": matches}

    except Exception as e:
        return {"matches": []}
