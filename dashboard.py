import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time

st.set_page_config(page_title="Crypto Dashboard", layout="wide")

def fetch_and_append_prices(sheet): #add data to google sheet
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    response = requests.get(url)
    prices = response.json()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append each coin's price as a row in the sheet
    for coin in prices:
        price = prices[coin]['usd']
        sheet.append_row([timestamp, coin, price])

# Fetch data from Google Sheets
def fetch_sheet_data():
    # Convert AttrDict to dict
    gcp_credentials = dict(st.secrets["gcp"])
    
    # Define scope and create credentials
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(gcp_credentials, scope)

    client = gspread.authorize(creds)
    sheet = client.open_by_key(st.secrets["sheet_id"]).sheet1
    fetch_and_append_prices(sheet)
    data = sheet.get_all_records()
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

# Live update every X seconds
REFRESH_INTERVAL = 60  # seconds
placeholder = st.empty()

while True:
    df = fetch_sheet_data()
    
    with placeholder.container():
        st.title("📈 Live Crypto Prices Dashboard")
        st.dataframe(df)

    time.sleep(REFRESH_INTERVAL)
