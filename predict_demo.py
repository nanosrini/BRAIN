import streamlit as st
from demo_data import PREDICTIONS

def show():
    st.title("🧠 AI Risk Predictions")

    st.caption("Conference Demo Mode")

    for p in PREDICTIONS:
        st.metric(
            label=p["disease"],
            value=f"{p['risk_score']}/100",
            delta=p["risk_level"]
        )