import streamlit as st
import requests

# 1. Config
st.set_page_config(page_title="Gold Intelligence Pro", layout="wide")

# 2. Telegram Settings (ဒီနေရာမှာ လူကြီးမင်းရဲ့ အချက်အလက် ထည့်ပါ)
TOKEN = "လူကြီးမင်းရဲ့_TOKEN_ဒီမှာထည့်"
CHAT_ID = "လူကြီးမင်းရဲ့_CHAT_ID_ဒီမှာထည့်"

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
