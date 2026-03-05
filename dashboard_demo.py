import streamlit as st
from demo_data import SUMMARY, PREDICTIONS
import streamlit.components.v1 as components

def show():

    st.markdown(
        "<h1 style='color:#000000;'>BRAIN — AI Surveillance Dashboard</h1>",
        unsafe_allow_html=True
    )

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

    st.markdown(
        "<h1 style='color:#000000;'>🧠 AI Risk Ranking</h1>",
        unsafe_allow_html=True
    )

    for disease in PREDICTIONS:
        progress_width = disease["risk_score"]

        html = f"""
        <div style="
            background:#F0F9FF;
            padding:18px;
            border-radius:18px;
            border:1px solid #E0F2FE;
            box-shadow:0 2px 6px rgba(0,0,0,0.04);
            margin-bottom:16px;
            font-family:sans-serif;
        ">

            <div style="
                display:flex;
                justify-content:space-between;
                align-items:center;
                font-size:16px;
                font-weight:600;
                color:#0F172A;
            ">
                <div>{disease['disease']}</div>

                <div style="
                    color:{disease['color']};
                    font-weight:700;
                ">
                    {disease['risk_level']}
                </div>
            </div>

            <div style="
                width:100%;
                background:#E5E7EB;
                height:8px;
                border-radius:6px;
                margin-top:12px;
                overflow:hidden;
            ">
                <div style="
                    width:{progress_width}%;
                    background:{disease['color']};
                    height:100%;
                "></div>
            </div>

            <div style="
                font-size:12px;
                color:#64748B;
                margin-top:8px;
            ">
                Risk Score: {disease['risk_score']}/100
            </div>

        </div>
        """

        components.html(html, height=130)
