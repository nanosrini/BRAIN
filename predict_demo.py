import streamlit as st
from demo_data import PREDICTIONS

def show():

    st.markdown(
        "<h1 style='color:#000000;'>🧠 AI Risk Predictions</h1>",
        unsafe_allow_html=True
    )

    for p in PREDICTIONS:
        st.metric(
            label=p["disease"],
            value=f"{p['risk_score']}/100",
            delta=p["risk_level"]
        )
