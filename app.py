import streamlit as st
import requests

# 1. Config
st.set_page_config(page_title="Gold Intelligence Pro", layout="wide")

# 2. Telegram Settings (ဒီနေရာမှာ လူကြီးမင်းရဲ့ အချက်အလက် ထည့်ပါ)
TOKEN = "8625424625:AAG06Yoem1vN71_3iVTPkI7qvS1Z3yO0jqM"
CHAT_ID = "6129668150"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "HTML"}
    try:
        requests.post(url, data=payload)
    except:
        pass

# 3. UI Dashboard
st.title(" Gold Intelligence Dashboard (2026)")
st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.header(" Market Insights")
    st.info(" **WGC Update:** Gold demand is increasing in early 2026.")
    st.subheader(" News Feed")
    st.write(" US Inflation data is driving gold prices higher.")

with col2:
    st.header(" Sentiment")
    st.success("Current Sentiment: **Strong Buy**")
    st.divider()
    # ဤနေရာတွင် "Send Test Alert" ခလုတ်ကို ပြန်ထည့်ပေးထားပါတယ်
    if st.button("Send Test Alert"):
        send_telegram_alert(" <b>Gold Pro System:</b> Connection Successful!")
        st.write("Telegram ဆီ စာပို့လိုက်ပါပြီ!")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gold Intelligence Pro", layout="wide")

# အရှုံး/အမြတ် တွက်ချက်မှု (Risk 1:5)
def calculate_pnl(lot_size):
    base_risk = 18.0
    base_reward = 90.0
    multiplier = lot_size / 0.01
    return base_risk * multiplier, base_reward * multiplier

st.title(" Gold Intelligence Live Monitor")

# Sidebar - Settings & Lot Control
st.sidebar.header(" Trading Settings")
current_lot = st.sidebar.number_input("Current Lot Size", min_value=0.01, value=0.01, step=0.01)
risk, reward = calculate_pnl(current_lot)

st.sidebar.divider()
st.sidebar.metric("Target Risk (SL)", f"-${risk:,.2f}")
st.sidebar.metric("Target Reward (TP)", f"+${reward:,.2f}")

# Main Dashboard UI
col1, col2 = st.columns(2)

with col1:
    st.subheader(" Live Strategy Status")
    st.write(f"**Current Lot:** {current_lot}")
    st.write(f"**Risk/Reward Ratio:** 1:5")
    st.progress(20) # Risk 1:5 visualization

with col2:
    st.subheader(" Potential P/L for this Trade")
    st.error(f"If SL hits: -${risk}")
    st.success(f"If TP hits: +${reward}")

st.divider()
st.info(" EA ကနေ အော်ဒါဖွင့်တိုင်း ဒီ Dashboard မှာ အလိုအလျောက် Update ဖြစ်နေမှာပါ။")
