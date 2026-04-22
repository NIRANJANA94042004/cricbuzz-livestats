import streamlit as st
from api.cricbuzz_api import get_live_matches

st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")

st.title("🏏 Cricbuzz LiveStats")

if st.button("Get Live Matches"):

    data = get_live_matches()
    matches = data.get("matches", [])

    if matches:
        st.subheader("📊 Live Matches")

        for match in matches:
            title = match.get("match_title", "")
            status = match.get("status", "")
            score_data = match.get("score", "")

            score_text = ""

            if isinstance(score_data, list):
                for team in score_data:
                    score_text += f"{team.get('short','')} {team.get('score','')}  "

            st.markdown(f"### 🏏 {title}")
            st.write(f"**Score:** {score_text}")
            st.write(f"**Status:** {status}")
            st.markdown("---")

    else:
        st.warning("No live matches available")
