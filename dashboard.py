import sqlite3
import pandas as pd
import streamlit as st

def load_from_db():
    conn = sqlite3.connect('crypto_data.db')                                            #connect to database
    df = pd.read_sql_query("SELECT * FROM crypto_prices", conn)                         #SQL query to get all prices stored in db
    conn.close()                                                                        #closing connection to avoid rate limits and to lower memory usage
    return df

st.title("Live Crypto-currency Price Tracker")
df = load_from_db()
df_deduped = df.drop_duplicates(subset=['timestamp', 'coin'])                           #removing duplicates; IFF every pricepoint is significant, group each price per timestamp and use mean instead of dropping
pivoted = df_deduped.pivot(index='timestamp', columns='coin', values='price_usd')
st.line_chart(pivoted)
