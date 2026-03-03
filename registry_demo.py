import streamlit as st
from demo_data import SAMPLES

def show():
    st.title("📋 Registry")

    st.caption("Conference Demo Mode — Sample Data")

    for s in SAMPLES:
        st.markdown(f"""
        <div style="
            background:#FFFFFF;
            padding:12px;
            border-radius:12px;
            border:1px solid #E2E8F0;
            margin-bottom:10px;
        ">
            <b style="color:#000000;">{s['disease']}</b><br>
            <span style="color:#64748B;font-size:12px;">
                {s['barcode']} • {s['sample_type']} • {s['collection_date']}
            </span>
        </div>
        """, unsafe_allow_html=True)