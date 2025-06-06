import gspread
import json
import pandas as pd
import requests
import datetime
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

def fetch_and_append_prices(sheet):                                                                                     #Get data and conert to JSON
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tron&vs_currencies=usd"
    response = requests.get(url)
    prices = response.json()

    Time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for coin in prices:                                                                                                 #Append data in each row
        price = prices[coin]['usd']
        sheet.append_row([Time_stamp, coin, price])

def fetch_sheet_data():                                                                                                 #Connecting and reading from Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = st.secrets["gcp"]                                                                                      #google cloud platform credential dictionary
    creds_json = json.dumps(dict(creds_dict))
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(creds_json), scope)
    client = gspread.authorize(creds)

    sheet = client.open("CryptoData").worksheet("PriceSheet")                                                           #Selecting workbook and worksheet to work with

    fetch_and_append_prices(sheet)

    data = sheet.get_all_records(expected_headers=["Time_stamp", "coin", "price"])                                      #Convert data to a pandas framework dataframe
    return pd.DataFrame(data)

st.title("📈 Live Crypto Prices Dashboard")                                                                             #Streamlit design and layout

df = fetch_sheet_data()

if not df.empty:                                                                                                        #render visuals
    df['Time_stamp'] = pd.to_datetime(df['Time_stamp'])
    df_deduped = df.drop_duplicates(subset=['Time_stamp', 'coin'])
    pivoted = df_deduped.pivot(index='Time_stamp', columns='coin', values='price')
    st.line_chart(pivoted)
else:
    st.warning("No data found in the Google Sheet.")
