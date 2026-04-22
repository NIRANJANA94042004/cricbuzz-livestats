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
            score = match.get("score", "")

            st.markdown(f"### 🏏 {title}")
            st.write(f"**Score:** {score}")
            st.write(f"**Status:** {status}")
            st.markdown("---")

    else:
        st.warning("😴 No Live Matches Right Now. Try later!")
