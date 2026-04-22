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

    # 🔥 Correct extraction logic
    for type_match in data.get("typeMatches", []):
        for series in type_match.get("seriesMatches", []):

            wrapper = series.get("seriesAdWrapper", {})

            for match in wrapper.get("matches", []):

                info = match.get("matchInfo", {})
                score = match.get("matchScore", {})

                team1 = info.get("team1", {}).get("teamName", "")
                team2 = info.get("team2", {}).get("teamName", "")
                status = info.get("status", "")

                score_text = ""

                # Team 1 score
                if score.get("team1Score"):
                    inng = score["team1Score"].get("inngs1", {})
                    score_text += f"{team1}: {inng.get('runs','')}/{inng.get('wickets','')}  "

                # Team 2 score
                if score.get("team2Score"):
                    inng = score["team2Score"].get("inngs1", {})
                    score_text += f"{team2}: {inng.get('runs','')}/{inng.get('wickets','')}"

                matches.append({
                    "match_title": f"{team1} vs {team2}",
                    "status": status,
                    "score": score_text
                })

    return {"matches": matches}
