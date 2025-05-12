import time
import json
from src.stock_scraper import get_stock_price
from src.stock_api import get_stock_price_from_api
from src.email_alert import send_email_alert
from src.stock_logger import log_stock_price

def monitor_stock():
    with open('config/settings.json') as f:
        config = json.load(f)
    
    stock_symbol = config["target_stock_symbol"]
    threshold = config["threshold"]
    api_key = config["stock_api_key"]
    
    while True:
        stock_price = get_stock_price_from_api(stock_symbol, api_key)
        print(f"Stock Price: {stock_price}")
        
        if stock_price > threshold:
            send_email_alert(
                subject=f"Stock Alert: {stock_symbol} Price Crossed {threshold}",
                body=f"The stock price for {stock_symbol} has reached {stock_price}",
                recipient_email=config["email"]
            )
        log_stock_price(stock_price, stock_symbol, "reports/stock_price_log.csv")
        time.sleep(60)

if __name__ == "__main__":
    monitor_stock()
