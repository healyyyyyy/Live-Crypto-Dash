import gspread
import json
import pandas as pd
import requests
import datetime
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Function to fetch live crypto prices and append to Google Sheet
def fetch_and_append_prices(sheet):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    prices = response.json()

    Time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append each coin's price as a row in the sheet
    for coin in prices:
        price = prices[coin]['usd']
        sheet.append_row([Time_stamp, coin, price])

# Function to connect and load Google Sheet data
def fetch_sheet_data():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = st.secrets["gcp"]
    creds_json = json.dumps(dict(creds_dict))
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(creds_json), scope)
    client = gspread.authorize(creds)

    # Open Google Sheet and target the 'prices' worksheet
    sheet = client.open("CryptoData").worksheet("PriceSheet")

    # Append latest data (Bitcoin and Ethereum prices)
    fetch_and_append_prices(sheet)

    # Load all data from sheet into DataFrame
    data = sheet.get_all_records(expected_headers=["Time_stamp", "coin", "price"])
    return pd.DataFrame(data)

# Streamlit app layout
st.title("📈 Live Crypto Prices Dashboard")

df = fetch_sheet_data()

# Preprocess and visualize
if not df.empty:
    df['Time_stamp'] = pd.to_datetime(df['Time_stamp'])
    df_deduped = df.drop_duplicates(subset=['Time_stamp', 'coin'])
    pivoted = df_deduped.pivot(index='Time_stamp', columns='coin', values='price')
    st.line_chart(pivoted)
else:
    st.warning("No data found in the Google Sheet.")
