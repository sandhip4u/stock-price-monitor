import requests

def get_stock_price_from_api(stock_symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_symbol}&interval=1min&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    latest_time = list(data["Time Series (1min)"].keys())[0]
    return float(data["Time Series (1min)"][latest_time]["1. open"])
