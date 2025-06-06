import gspread
import json
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

def fetch_sheet_data():   
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # Load from secrets
    creds_dict = st.secrets["gcp"]
    creds_json = json.dumps(creds_dict)
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(creds_json), scope)
    client = gspread.authorize(creds)                                                                          #Using creds to access worksheet
    sheet = client.open("CryptoData").worksheet("prices")
    data = sheet.get_all_records()
    return pd.DataFrame(data)

st.title("Live Crypto-currency Price Tracker")
df = fetch_sheet_data()
df['timestamp'] = pd.to_datetime(df['timestamp'])
df_deduped = df.drop_duplicates(subset=['timestamp', 'coin'])                                                   #removing dupliacate values; IFF every pricepoint is significant, instead of removing duplicates group by timestamp and use mean
pivoted = df_deduped.pivot(index='timestamp', columns='coin', values='price_usd')
st.line_chart(pivoted)
