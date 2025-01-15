import requests

# ...existing code...

def fetch_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data['bitcoin']['usd']

# ...existing code...
a = fetch_bitcoin_price()
print(a)