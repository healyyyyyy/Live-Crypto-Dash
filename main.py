import time
from datetime import datetime
from extract import fetch_crypto_data
from transform import transform_data
from load import load_data

def run_pipeline():
    raw = fetch_crypto_data()                   #Extract via API
    cleaned = transform_data(raw)               #Filter for USD rate and drop duplicates
    load_data(cleaned)                          
    print(f"[{datetime.now().isoformat()}] ETL run complete.")

if __name__ == '__main__':
    while True:
        try:
            run_pipeline()
            time.sleep(300)                     #Wait 5 mins per update
        except Exception as e:
            print("Error during ETL run:", e)
            time.sleep(60)                      #Wait 1 min before retrying
