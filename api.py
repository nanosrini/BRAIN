import requests
import streamlit as st
from components.html import render_html

# Change this if deployed
API_BASE = "http://127.0.0.1:8000/api"

TIMEOUT = 5


# ─────────────────────────────────────
# GET
# ─────────────────────────────────────

def api_get(path, params=None):
    try:
        r = requests.get(f"{API_BASE}{path}", params=params, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()

    except requests.ConnectionError:
        st.error("⚠️ Backend offline. Run: uvicorn main:app --reload")
        return None

    except requests.HTTPError as e:
        st.error(f"API Error {r.status_code}: {r.text}")
        return None

    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        return None


# ─────────────────────────────────────
# POST
# ─────────────────────────────────────

def api_post(path, data):
    try:
        r = requests.post(f"{API_BASE}{path}", json=data, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()

    except requests.ConnectionError:
        st.error("⚠️ Cannot connect to backend.")
        return None

    except requests.HTTPError:
        st.error(f"API Error {r.status_code}: {r.text}")
        return None

    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        return None


# ─────────────────────────────────────
# PATCH
# ─────────────────────────────────────

def api_patch(path, data=None):
    try:
        r = requests.patch(f"{API_BASE}{path}", json=data or {}, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()

    except requests.ConnectionError:
        st.error("⚠️ Backend not reachable.")
        return None

    except requests.HTTPError:
        st.error(f"API Error {r.status_code}: {r.text}")
        return None

    except Exception as e:
        st.error(f"Unexpected Error: {e}")
        return None