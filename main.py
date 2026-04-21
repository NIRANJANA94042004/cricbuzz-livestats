import streamlit as st
from api.cricbuzz_api import get_live_matches

st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")

st.title("🏏 Cricbuzz LiveStats")

if st.button("Get Live Matches"):
    data = get_live_matches()

    try:
        # 👉 FIRST matches create pannuvom
        matches = data.get("matches", [])

        if matches:
            st.subheader("📊 Live Matches")

            for match in matches:

                # 👉 TEAM
                title = match.get("match_title", "")
                if " vs " in title:
                    team1, team2 = title.split(" vs ")
                else:
                    team1, team2 = "N/A", "N/A"

                # 👉 STATUS
                status = match.get("status", "N/A")

                # 👉 SCORE FIX 🔥
                score_data = match.get("score", "")
                score_text = ""

                if isinstance(score_data, list):
                    for team_score in score_data:
                        runs = team_score.get("score", "")
                        short = team_score.get("short", "")
                        score_text += f"{short}: {runs}   "

                elif isinstance(score_data, str):
                    score_text = score_data

                if score_text == "" or score_text == "No score available":
                    score_text = status

                # 👉 UI
                st.markdown(f"""
                <div style="
                    border:1px solid #ddd;
                    border-radius:10px;
                    padding:15px;
                    margin-bottom:10px;
                    background-color:#f9f9f9;
                ">
                    <h4>🏏 {team1} vs {team2}</h4>
                    <p><b>Live Info:</b> {score_text}</p>
                    <p><b>Status:</b> {status}</p>
                </div>
                """, unsafe_allow_html=True)

        else:
            st.warning("😴 No Matches Found")

    except Exception as e:
        st.error("❌ Error")
        st.write(e)