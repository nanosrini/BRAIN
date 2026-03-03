import streamlit as st
import streamlit.components.v1 as components

import dashboard_demo
import registry_demo
import predict_demo


st.set_page_config(
    page_title="BRAIN - Demo",
    page_icon="🧬",
    layout="centered"
)

# Global Style
st.markdown("""
<style>
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stSidebar"] {
    background-color: #FFFFFF;
}
</style>
""", unsafe_allow_html=True)

# Initialize screen
if "screen" not in st.session_state:
    st.session_state.screen = "login"

# Navigation helper
def go(screen):
    st.session_state.screen = screen
    st.rerun()

# ─────────────────────────────────────────
# Hamburger (Not on Login)
# ─────────────────────────────────────────

if st.session_state.screen != "login":
    col1, col2 = st.columns([1, 9])

    with col1:
        if st.button("☰"):
            st.session_state.menu_open = not st.session_state.get("menu_open", False)

# ─────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────

if st.session_state.get("menu_open", False):
    with st.sidebar:
        st.title("🧬 BRAIN Demo")

        if st.button("Dashboard"):
            go("home")

        if st.button("Registry"):
            go("registry")

        if st.button("AI Predictions"):
            go("predict")

        st.markdown("---")
        st.caption("Conference Demo Mode")

# ─────────────────────────────────────────
# Login Screen
# ─────────────────────────────────────────

if st.session_state.screen == "login":

    components.html("""
    <div style="
        height:85vh;
        display:flex;
        flex-direction:column;
        justify-content:center;
        align-items:center;
        font-family:-apple-system, BlinkMacSystemFont, sans-serif;
        text-align:center;
    ">
        <div style="font-size:64px;">🧬</div>

        <div style="
            font-size:34px;
            font-weight:800;
            color:#111827;
            margin-top:12px;
        ">
            BRAIN
        </div>

        <div style="
            font-size:14px;
            color:#6B7280;
            letter-spacing:1px;
            margin-top:8px;
        ">
            Biobank Realtime Artificial Intelligence Network
        </div>
    </div>
    """, height=600)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("""
        <style>
        div.stButton > button {
            width:100%;
            background:#111827 !important;
            color:#FFFFFF !important;
            padding:14px !important;
            border-radius:10px !important;
            border:none !important;
            font-size:16px !important;
            font-weight:600 !important;
        }
        </style>
        """, unsafe_allow_html=True)

        if st.button("🔐 Login"):
            go("home")

    st.stop()

# ─────────────────────────────────────────
# Router
# ─────────────────────────────────────────

if st.session_state.screen == "home":
    dashboard_demo.show()

elif st.session_state.screen == "registry":
    registry_demo.show()

elif st.session_state.screen == "predict":
    predict_demo.show()
