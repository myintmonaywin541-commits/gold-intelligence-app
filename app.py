import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Layout သတ်မှတ်ခြင်း
st.set_page_config(page_title="Gold Intelligence Pro", layout="wide")
TOKEN ="8792478423:AAGOx_GVloS9xdMWmP2Fe5Y6_cMdQ3q3Ecs"
CHAT_ID = "6129668150"

# Sidebar - Live Status
st.sidebar.title(" XAU/USD Monitor")
st.sidebar.metric("Live Price", "5278.50", "+1.2%")
st.sidebar.write("EA Status: **ACTIVE (Lot 0.05)**")
st.sidebar.write("Current Signal: **BULLISH**")

# Main Dashboard
st.title(" Gold Market Intelligence Dashboard (2026)")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.header(" World Gold Council (WGC) Insights")
    try:
        # WGC မှ Data ဆွဲယူခြင်း (Example Logic)
        st.info(" Central Banks increased gold reserves by 15% this quarter.")
        st.success(" ETF Inflows: Positive momentum in Western markets.")
    except:
        st.write("WGC Data Fetching...")

    st.header(" High Impact Fundamental News")
    # News Feed
    news = [
        {"time": "10:30 AM", "event": "US PCE Data lower than expected", "impact": "Bullish"},
        {"time": "02:15 PM", "event": "Geopolitical tension in Middle East", "impact": "High Bullish"},
        {"time": "04:00 PM", "event": "DXY Dollar Index Weakness", "impact": "Moderate Bullish"}
    ]
    for item in news:
        st.write(f"**{item['time']}** - {item['event']} | *Impact: {item['impact']}*")

with col2:
    st.header(" EA Strategy (M5)")
    st.write("**Strategy:** EMA 161/423 Cross")
    st.write("**SL/TP:** 180 / 900 Pips")
    
    # Sentiment Meter
    st.subheader("Market Sentiment")
    st.progress(85) # 85% Bullish
    st.write("Current Sentiment: **Strong Buy**")

st.divider()
st.caption("Developed for Professional Gold Trading - 2026 Strategy")
    st.divider()
    st.header(" Telegram Controls")
    if st.button("Send Test Alert"):
        send_telegram_alert(" <b>Gold Pro System:</b> Dashboard Connected Successfully!")
        st.write("Alert Sent to your phone!")
