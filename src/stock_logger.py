import csv
import os
from datetime import datetime

def log_stock_price(price, stock_symbol, file_path):
    fieldnames = ['Stock Symbol', 'Price', 'Timestamp']
    exists = os.path.isfile(file_path)
    
    with open(file_path, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        writer.writerow({
            'Stock Symbol': stock_symbol,
            'Price': price,
            'Timestamp': datetime.now().isoformat()
        })
