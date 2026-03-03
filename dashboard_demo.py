import streamlit as st
from demo_data import SUMMARY, PREDICTIONS
import streamlit.components.v1 as components

def show():

    st.title("BRAIN — AI Surveillance Dashboard")

    col1, col2, col3, col4 = st.columns(4)



    def stat_card(title, value, subtitle, value_color="#111827"):
        html = f"""
        <div style="
            background:#F0F9FF;
            padding:16px;
            border-radius:14px;
            border:1px solid #E0F2FE;
            box-shadow:0 1px 4px rgba(0,0,0,0.04);
            font-family: sans-serif;
        ">
            <div style="font-size:13px;color:#64748B;">
                {title}
            </div>

            <div style="
                font-size:26px;
                font-weight:700;
                margin-top:4px;
                color:{value_color};
            ">
                {value}
            </div>

            <div style="
                font-size:12px;
                color:#94A3B8;
                margin-top:4px;
            ">
                {subtitle}
            </div>
        </div>
        """

        components.html(html, height=120)    # ───────── Stat Cards ─────────

    with col1:
        stat_card(
            "Total Samples",
            SUMMARY["total_samples"],
            f"{SUMMARY['positive_samples']} positive"
        )

    with col2:
        stat_card(
            "Active Alerts",
            SUMMARY["active_alerts"],
            f"{SUMMARY['critical_alerts']} critical",
            value_color="#DC2626"
        )

    with col3:
        stat_card(
            "Positivity Rate",
            f"{SUMMARY['positivity_rate']}%",
            "All-time avg"
        )

    with col4:
        stat_card(
            "Diseases Tracked",
            SUMMARY["diseases_tracked"],
            "Active surveillance"
        )

    # ─────────────────────────────────────────
    # 🧠 AI RISK RANKING
    # ─────────────────────────────────────────

    st.subheader("🧠 AI Risk Ranking")

    for disease in PREDICTIONS:
        with st.container(border=True):
            c1, c2 = st.columns([4, 1])

            with c1:
                st.markdown(f"**{disease['disease']}**")

            with c2:
                st.markdown(
                    f"<span style='color:{disease['color']}; font-weight:700;'>"
                    f"{disease['risk_level']}</span>",
                    unsafe_allow_html=True
                )

            st.progress(disease["risk_score"] / 100)
            st.caption(f"Risk Score: {disease['risk_score']}/100")