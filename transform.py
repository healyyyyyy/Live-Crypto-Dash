from datetime import datetime

def transform_data(raw_data):
    transformed = []                                                                #initialize empty tuple
    for coin, info in raw_data.items():                                             #loop to store USD exchange rates
        price = info['usd']                                                         #storing USD exchange rate as 'price' variable
        timestamp = datetime.fromtimestamp(info['last_updated_at']).isoformat()     #formatting date and time for precision
        transformed.append({                                                        #pushing formatted data to our tuple
            'coin': coin,
            'price_usd': price,
            'timestamp': timestamp
        })
    return transformed
