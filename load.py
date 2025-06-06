import gspread
from oauth2client.service_account import ServiceAccountCredentials

def load_data(data):                                                                                            #Reading data stored in Google Sheet
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name("dark-star-462021-r3-2dad6644a32a.json", scope)    #authorizing Google API to read / write in sheet
    client = gspread.authorize(creds)
    sheet = client.open("CryptoData").worksheet("PriceSheet")

    for row in data:
        sheet.append_row([row['coin'], row['price_usd'], row['timestamp']])                                     #Writing returned data from API into Google Sheet