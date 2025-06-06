import requests

def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/simple/price'           #CoinGecko API
    params = {                                                      #Selecting parameters to extract
        'ids': 'bitcoin,ethereum,tron',
        'vs_currencies': 'usd',
        'include_last_updated_at': 'true'
    }
    response = requests.get(url, params=params)                     #Storing returned data as a variable
    return response.json()                                          #Converting raw data into JSON for better readability